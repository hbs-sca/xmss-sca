#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import math
import numpy as np
from os import listdir
from os.path import isfile, join
import matplotlib.pyplot as plt


def parse_csv(file):
    ifile = open(file, "rb")
    reader = csv.reader(ifile, delimiter=';')
    values = []
    for row in reader:
        values.append(np.array([int(row[0]), row[3]]))
    ifile.close()
    return np.array(values)

def scatter_txt(x,y):
    txt = ""
    for p, d in zip(x, y):
        txt += "\nn=%d p=%.3f" % (p, d)
    return txt

def plot_scatter(x, y, fname):
    f = plt.figure(figsize=(11,5))
    plt.plot(x,y, "x", ms=18.0)
    plt.ylabel("success probability")
    plt.xlabel("number of traces")
    plt.ylim(ymin=0)
    plt.ylim(ymax=1.1)
    plt.tight_layout()
    plt.figtext(.7, .2, scatter_txt(x, y))
    #plt.show()
    f.savefig(fname)


#experiment 2


n = [8,10,16,32,64,128,256,512]

d = []
for i in n:
    data = np.array(parse_csv("../data/exp_2/%d.log" %i)[:, 0], dtype=np.float)
    d.append(data.sum() / len(data))
plot_scatter(n,d, "dpa_exp_2.pdf")

# experiment 6
n = [16, 32, 64, 96, 128, 256, 512, 1024, 2048, 4048, 8096]
d = []
for i in n:
    data =  np.array(parse_csv("../data/exp_6/%d.log" %i)[:, 0], dtype=np.float)
    d.append(data.sum() / len(data))
plot_scatter(n,d, "dpa_exp_6.pdf")
