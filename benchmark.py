# ラズパイの演算速度の検証用

import numpy as np
import time

def vector_dot():
    st = time.time()
    for i in range(100000):
        a = np.random.random(300)
        b = np.random.random(300)
        c = np.dot(a,b)
    print('Executed time: ', time.time()-st, 'sec')

if __name__ == '__main__':
    vector_dot()