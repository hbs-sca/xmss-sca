#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import numpy as np
import matplotlib.pyplot as plt

def load_trace(file_name):
    f = open(file_name, "r")
    a = np.fromfile(f, dtype=np.uint8)
    return a

T = load_trace("../data/sample_trace")
f = plt.figure(figsize=(11, 5))

plt.subplot(2,1,1)
fig1 = plt.plot(T)
plt.ylabel("hamming weight")
plt.xlabel("index of sample")


plt.subplot(2,1,2)
fig2 = plt.plot(range(4300, 4600), T[4300:4600])
plt.ylabel("hamming weight")
plt.xlabel("index of sample")
plt.tight_layout()

f.savefig("power_trace_plot.pdf")
