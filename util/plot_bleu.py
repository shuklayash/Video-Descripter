import numpy as np
import matplotlib.pyplot as plt
import os

file = open('plot_bleu.txt', 'r')
l = []
for line in file.readlines():
    l.append(float(line.split('\n')[0]))

l = np.array(l)
plt.plot(l)
plt.title('BLEU score (Our score: 0.7049411)')
plt.xlabel('epoch')
plt.ylabel('BLEU score')
plt.savefig('bleu-plot.png')