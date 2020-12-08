# -*- coding: utf-8 -*-

from kd_mpc_handler import KdMpcHandler

print("import success!")


import numpy as np

handler = KdMpcHandler(address="127.0.0.1", port1=50003, port2=50004, role=False, f=1, num_workers=2, k=5)
handler.init_sru_aby()
handler.init_kd_aby()

# test1 = np.random.randint(2, size=100000).tolist()
#
# for i in range(10):
#     rst = handler.kd_sru(idx=test1)
#     print(i, ":", len(rst))

ograd = (50 - np.random.randint(100, size=10))
print("ograd", ograd)
test2 = []
test2 += handler.kd_top(grad=ograd)
print(test2)
print("=" * 50)
handler.shutdown_aby()
