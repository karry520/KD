# -*- coding: utf-8 -*-

import time
import torch
import torchvision
from torch import nn, optim, autograd

import grpc
from Grpc.kd_pb2 import GradRequest, GradResponse, IdxRequest, IdxResponse
from Grpc.kd_pb2_grpc import Collaborative_LearningStub

from Model.LeNet import LeNet
from Utils.data_loader import load_data_fashion_mnist
from Utils.evaluate import evaluate_accuracy
from Utils.edcode import encode, decode

import numpy as np

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

FRAC = 1000
status = 0


class Node(object):

    def __init__(self, model, train_iter, test_iter, num_epochs, topk, optimizer=None, device=None, stub1=None,
                 stub2=None):

        self.device = device
        self.loss_func = nn.CrossEntropyLoss()
        self.model = model.to(self.device)
        self.optimizer = optimizer
        self.train_iter = train_iter
        self.test_iter = test_iter
        self.num_epochs = num_epochs

        self.stub1 = stub1
        self.stub2 = stub2

        self.topk = topk

        self.level_length = [0]
        self.gradients = []

        self.grad_topk = []
        self.grad_idx = []

        self.grad_len = 0

    def train_step(self, X, y):

        X = X.to(self.device)
        y = y.to(self.device)

        y_hat = self.model(X)
        loss = self.loss_func(y_hat, y)
        self.optimizer.zero_grad()
        loss.backward()

        self.gradients = []
        self.level_length = [0]
        self.grad_topk = []
        self.grad_idx = []

        for param in self.model.parameters():
            self.level_length.append(param.grad.numel() + self.level_length[-1])
            self.gradients += param.grad.view(-1).numpy().tolist()

        self.grad_len = len(self.gradients)
        grad_abs = np.abs(self.gradients)
        index = np.argpartition(grad_abs, self.topk)[0 - self.topk:]
        self.grad_idx = np.zeros(self.grad_len, dtype=int)

        for idx in index:
            self.grad_idx[idx] = 1

        return loss.cpu().item(), y_hat

    def updateidx(self):
        share_idx1 = np.random.randint(2, size=self.grad_len).tolist()
        share_idx2 = np.array(np.logical_xor(self.grad_idx, share_idx1), dtype=int).tolist()

        print("update idx begging")
        idx_upd_res1 = self.stub1.UpdateIdx.future(IdxRequest(idx_ori=encode(share_idx1)))
        idx_upd_res2 = self.stub2.UpdateIdx(IdxRequest(idx_ori=encode(share_idx2)))
        print("update idx end")
        return idx_upd_res1.result().idx_upd, idx_upd_res2.idx_upd

    def updategrad(self, idx_upd1, idx_upd2):
        dc_idx_upd1 = decode(idx_upd1)
        dc_idx_upd2 = decode(idx_upd2)
        idx_upd = np.array(np.logical_xor(dc_idx_upd1[:self.grad_len], dc_idx_upd2[:self.grad_len]), dtype=int)

        self.grad_idx = idx_upd.tolist()

        idx_upd = np.nonzero(idx_upd)[0]
        grad_top = np.array(self.gradients)[idx_upd]

        grad_top = np.array(grad_top * FRAC, dtype=int)

        share_grad1 = np.random.randint(100, size=len(idx_upd))
        share_grad2 = grad_top - share_grad1

        print("update grad beginning")
        grad_upd_res1 = self.stub1.UpdateGrad.future(GradRequest(grad_ori=share_grad1.tolist()))
        grad_upd_res2 = self.stub2.UpdateGrad(GradRequest(grad_ori=share_grad2.tolist()))
        print("update grad end!")
        return grad_upd_res1.result().grad_upd, grad_upd_res2.grad_upd

    def upgrade(self, grad_upd1, grad_upd2):

        grad_upd = np.array(np.array(grad_upd1) + np.array(grad_upd2), dtype=float)

        grad_upd = np.array(grad_upd / FRAC)
        idx_upd = np.nonzero(self.grad_idx)[0]

        np.array(self.gradients)[idx_upd] = [grad_upd]

        idx = 0
        for param in self.model.parameters():
            tmp = self.gradients[self.level_length[idx]:self.level_length[idx + 1]]
            grad_re = torch.tensor(tmp)
            grad_re = grad_re.view(param.grad.size())

            param.grad = grad_re
            idx += 1

        self.optimizer.step()

    def train(self):
        for epoch in range(self.num_epochs):
            counter = 0
            train_l_sum, train_acc_sum, n, batch_count, start = 0.0, 0.0, 0, 0, time.time()
            for X, y in self.train_iter:
                counter += 1
                if int(counter % 10) == 0:
                    print("update:", counter)
                    loss, y_hat = self.train_step(X, y)
                    idx_upd_res1, idx_upd_res2 = self.updateidx()
                    grad_upd_res1, grad_upd_res2 = self.updategrad(idx_upd_res1, idx_upd_res2)

                    self.upgrade(grad_upd_res1, grad_upd_res2)
                    train_l_sum += loss
                    train_acc_sum += (y_hat.argmax(dim=1) == y).sum().cpu().item()
                    n += y.shape[0]
                    batch_count += 1
                    continue

                X = X.to(device)
                y = y.to(device)
                y_hat = self.model(X)
                l = self.loss_func(y_hat, y)
                self.optimizer.zero_grad()
                l.backward()
                self.optimizer.step()
                train_l_sum += l.cpu().item()
                train_acc_sum += (y_hat.argmax(dim=1) == y).sum().cpu().item()
                n += y.shape[0]
                batch_count += 1

            test_acc = evaluate_accuracy(self.test_iter, self.model)
            print('epoch %d, loss %.4f, train acc %.3f, test acc %.3f, time %.1f sec'
                  % (epoch + 1, train_l_sum / batch_count, train_acc_sum / n, test_acc, time.time() - start))
