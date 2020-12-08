# -*- coding: utf-8 -*-

import cppimport
import cppimport.import_hook
import Mpc.KD as m

print("\n Successfuly imported c++ code!")

import numpy as np

PMAX = 2 ** 10


class KdMpcHandler():
    def __init__(self, role, address, port1, port2, f, num_workers, k):
        self.role = role
        self.address = address
        self.port1 = port1
        self.port2 = port2
        self.num_workers = num_workers
        self.f = f
        self.k = k

    def init_sru_aby(self):
        m.init_aby(self.address, self.port1, self.role)

    def init_kd_aby(self):
        m.init1_aby(self.address, self.port2, self.role)

    def shutdown_aby(self):
        m.shutdown_aby()

    def kd_sru(self, idx):
        length = int(len(idx) / self.num_workers)

        rst = []
        in_idx = m.VectoruInt(idx)
        rst += m.kd_sru(self.role, in_idx, self.num_workers, length, self.f)

        return rst

    def kd_top(self, grad):
        length = int(len(grad) / self.num_workers)
        rst = []
        grad = np.array(grad) + PMAX
        print("grad:", grad)
        fgrad = np.array(grad) * 0.2
        fgrad = np.array(fgrad, dtype='int16')
        in_grad = m.VectoruInt32(grad.tolist())
        in_fgrad = m.VectoruInt32(fgrad.tolist())
        rst += m.kd_top(self.role, in_grad, in_fgrad, length, self.num_workers, self.f)
        rst = (np.array(rst) - (2 * self.f * PMAX)) / (2 * self.f)
        rst = np.array(rst, dtype='int32')
        return rst.tolist()
