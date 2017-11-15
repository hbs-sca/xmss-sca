#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


#./simulation/simulate 500 HW_BYTE 33c0364151e93bbda2896900f18c987737593ff2abc2f8a2220f54c58aa71968
##### SIMULATING POWER TRACE #####
#seed=0x33c0364151e93bbda2896900f18c987737593ff2abc2f8a2220f54c58aa71968
#leakage_type=3
#Creating 500 traces
#iv[0]=0x6a09e667bb67ae853c6ef372a54ff53a510e527f9b05688c1f83d9ab5be0cd19
#iv[1]=0x13e087020936aab9a2ecc5396601faf1a919aa0e8f4074c1e21173981cce9431
#a_0=0x13e08702
#b_0=0x0936aab9
#c_0=0xa2ecc539
#d_0=0x6601faf1
#e_0=0xa919aa0e
#f_0=0x8f4074c1
#g_0=0xe2117398
#h_0=0x1cce9431
#delta=0x21fd7822
#T2=0x42d93dc4
#leakage_500.bin

#./analysis/analyze_8bit.py leakage_500.bin secret_data.txt

R = np.load("../data/correlation_values.npy")
R[np.isnan(R)] = 0
R = np.absolute(R)
print R.shape

correct_hyp = R[:, 0x22]
wrong_hyp   = R[:, 0x42]
print correct_hyp[0:10];


def plot_overtime(d, fname):

    plt.plot(d)


# correlation over time
f, axarr = plt.subplots(2, sharex=True, figsize=(11,5))
axarr[0].plot(correct_hyp)
axarr[0].set_title("correct hypothesis (34)")
axarr[1].plot(wrong_hyp)
axarr[1].set_title("wrong hypothesis (66)")
plt.xlim(xmin=17000)
plt.xlim(xmax=32000)
plt.ylim(ymax=1.0)
# dummy subplot for the axis
ax = f.add_subplot(111, frameon=False)
ax.set_yticklabels([])
ax.set_xticklabels([])
ax.set_ylabel("Pearson correlation coefficient",labelpad=25)
plt.xlabel("index of sample",labelpad=20)
plt.tight_layout()
f.savefig("correlation_over_time.pdf")


# correlation of different hyptohesis
f = plt.figure(figsize=(11,3.5))
print np.where(R == 1.0)
d = R[20980, :]
plt.bar(range(0,256), d, edgecolor="none")
plt.xlabel("key hypothesis")
plt.ylabel("Pearon correlation coefficient")
plt.xlim(xmax=255)
plt.tight_layout()

f.savefig("max_correlation.pdf");
