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
    return values


def parse_all(path):
    values = [];
    for f in listdir(path):
        file = join(path, f)
        if isfile(file) and file.endswith(".log"):
            values.extend(parse_csv(file))
    return np.array(values)


def plot_scatter(x, y, fname):
    f = plt.figure(figsize=(11,5))

    plt.plot(x,y, color="lightgrey")
    plt.plot(x,y, "x", ms=9.0,clip_on=False)
    plt.ylabel("success probability")
    plt.xlabel("number of traces")
    plt.ylim(ymin=0)
    plt.ylim(ymax=1.1)

    table_data = map(lambda (T,p): ["%d"%T, "%.3f"%p],  zip(x,y))
    col_labels = ["T", "success rate"]

    table = plt.table(cellText=table_data, colWidths = [0.14,0.14],
              colLabels=col_labels, loc='center right')
    table.auto_set_font_size(False)
    table.set_fontsize(13)
    table.scale(1, 1.35)
    #plt.text(.7, .2, scatter_txt(x, y))

    plt.tight_layout()
    #plt.show()
    f.savefig(fname)



# experiment 1

n = [8,10,16,32,64,128,256,512]
d = []
for i in n:
    data = np.array(parse_all("../data/exp_1/%d/" %i)[:, 0], dtype=np.float)
    d.append(data.sum() / len(data))

plot_scatter(n,d, "dpa_exp_1.pdf")


# experiment 3
n = [16, 32, 64, 96, 128, 256, 512, 1024, 2048]
d = []
for i in n:
    data = np.array(parse_all("../data/exp_3/%d/" %i)[:, 0], dtype=np.float)
    d.append(float(data.sum()) / len(data))
plot_scatter(n,d, "dpa_exp_3.pdf")



# experiment 5
n = [16, 96, 128, 256, 512, 1024, 2048, 4048, 8096]
d = []
for i in n:
    data =  np.array(parse_all("../data/exp_5/%d/" %i)[:, 0], dtype=np.float)
    d.append(data.sum() / len(data))
plot_scatter(n,d, "dpa_exp_5.pdf")



# data pre-proc
good_seeds_file = open("../data/good_seeds_exp1.txt", "w")
data = parse_all("../data/exp_1/512/")
for sample in data:
    if sample[0] == '1':
        print>>good_seeds_file, (sample[1].replace("0x", ""))

good_seeds_file.close()

good_seeds_file = open("../data/good_seeds_exp5.txt", "w")
data = parse_all("../data/exp_5/8096/")
for sample in data:
    if sample[0] == '1':
        print>>good_seeds_file, (sample[1].replace("0x", ""))
good_seeds_file.close()
