import grpc
import time
from concurrent import futures
from Grpc.kd_pb2_grpc import add_Collaborative_LearningServicer_to_server
from server import Server
from Mpc.kd_mpc_handler import KdMpcHandler

import config

if __name__ == "__main__":

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    handler = KdMpcHandler(address="127.0.0.1", port1=50005, port2=50006, role=True, f=config.f, num_workers=config.num_workers, k=config.top_k)
    server1 = Server(kdmpchandler=handler)
    add_Collaborative_LearningServicer_to_server(server1, server)
    server.add_insecure_port('[::]:50000')
    server.start()

    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)
