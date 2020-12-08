# -*- coding: utf-8 -*-

import time
import torch

import grpc
from Grpc.kd_pb2 import GradRequest, GradResponse
from Grpc.kd_pb2_grpc import Collaborative_LearningStub

from Model.LeNet import LeNet
from Utils.data_loader import load_data_fashion_mnist
from Node import Node

import numpy

import config

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

if __name__ == "__main__":
    model = LeNet()
    batch_size = 512
    train_iter, test_iter = load_data_fashion_mnist(batch_size=batch_size)
    lr, num_epochs = 0.001, 5
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    with grpc.insecure_channel("localhost:50000") as channel1:
        with grpc.insecure_channel("localhost:50001") as channel2:
            print("connect success!")
            stub1 = Collaborative_LearningStub(channel1)
            stub2 = Collaborative_LearningStub(channel2)

            node = Node(model=model, train_iter=train_iter, test_iter=test_iter, num_epochs=num_epochs,
                        topk=config.top_k,
                        optimizer=optimizer, device=device, stub1=stub1, stub2=stub2)
            node.train()
