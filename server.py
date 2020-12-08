from Grpc.kd_pb2 import IdxResponse, GradResponse
from Grpc.kd_pb2_grpc import Collaborative_LearningServicer, add_Collaborative_LearningServicer_to_server

import threading

from Utils.edcode import decode, encode
import config

con = threading.Condition()
con1 = threading.Condition()

num = 0
round0 = 0

num1 = 0
round1 = 0

node_idx_ori = []
node_idx_upd = []
node_grad_ori = []
node_grad_upd = []
idx_rst = []
grad_rst = []


class Server(Collaborative_LearningServicer):

    def __init__(self, kdmpchandler):
        super(Server, self).__init__()
        self.kdmpchandler = kdmpchandler
        self.kdmpchandler.init_sru_aby()
        self.kdmpchandler.init_kd_aby()

    def UpdateIdx(self, request, context):
        print("update idx")
        global node_idx_ori
        global node_idx_upd

        node_idx_ori += decode(request.idx_ori)

        global num
        global round0

        con.acquire()
        num += 1
        if num < config.num_workers:
            con.wait()
        else:
            idx_ori = node_idx_ori
            print(len(idx_ori))
            node_idx_ori = []
            print("computing sru")
            node_idx_upd = self.kdmpchandler.kd_sru(idx=idx_ori)
            num = 0
            round0 += 1

            con.notifyAll()

        con.release()

        print("computer round :", round0)
        return IdxResponse(idx_upd=encode(node_idx_upd))

    def UpdateGrad(self, request, context):
        print("update grad")
        global node_grad_ori
        global node_grad_upd

        node_grad_ori += request.grad_ori

        global num
        global round1

        con.acquire()
        num += 1
        if num < config.num_workers:
            con.wait()
        else:
            grad_ori = node_grad_ori
            print(len(grad_ori))
            print(grad_ori)
            node_grad_ori = []
            print("computing top")
            node_grad_upd = self.kdmpchandler.kd_top(grad=grad_ori)

            num = 0
            round1 += 1
            con.notifyAll()

        con.release()
        print("node_grad_upd:", node_grad_upd)
        print("computer round1 :", round1)

        return GradResponse(grad_upd=node_grad_upd)
