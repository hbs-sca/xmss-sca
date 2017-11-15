#!/usr/bin/python
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

M = []
r = range(10,1600,10)
for i in r:
    d = np.load("../data/exp_7/%d.npy"%i);
    M.append(d)

M = np.matrix(M).T
plt.style.use('classic')
f = plt.figure(figsize=(11,5))
for i in range(0,256):
    if i == 0xA6:
        plt.plot(r, M[i,:].T, c='r')
    else:
        plt.plot(r, M[i,:].T, c='b', alpha=0.4-i*(0.3/256.0))
#plt.plot(range(10,1000,10), M[0xA6,:].T)
#plt.plot(range(10,1000,10), M[0xA7,:].T)

plt.ylabel("maximum Pearson correlation coefficient")
plt.xlabel("number of traces")
f.savefig("partial_corr.pdf");
