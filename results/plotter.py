import matplotlib.pyplot as plt
import numpy as np
import random
from math import sqrt

from scipy.interpolate import interp1d

k = [5, 15, 50, 100, 250, 750]

inter_k = np.linspace(5, 750, 2000)


scatter_time = [
        215.70839834400067,
        46.53546334400016,
        475.544533055001,
        18.22989998400044,
        112.05848896899988,
        1855.0883626369996 
]
scatter_time.sort()

f_scatter = interp1d(k, scatter_time, kind='cubic')
scatter_y = f_scatter(inter_k)


greedy_time = [
        205.38555010900018,
        33.22456170800069,
        470.6715945319993,
        10.21212264300084,
        105.51224854999964,
        1456.4788444219994        
]
greedy_time.sort()


f_greedy = interp1d(k, greedy_time, kind='cubic')
greedy_y = f_greedy(inter_k)

berkley_time = [
        72.45294282000032,
        54.29999575399961,
        82.1881860859994,
        40.34093231999941,
        67.89763072200003,
        84.95730442199965
]
berkley_time.sort()
f_berkley = interp1d(k, berkley_time, kind='cubic')
berkley_y = f_berkley(inter_k)

tabu_time = [
        477.5546083190002,
        95.06177055700027,
        1119.5415666919998,
        46.76725539399922,
        241.74723613199967,
        3487.1807830849993
]
tabu_time.sort()
f_tabu = interp1d(k, tabu_time, kind='cubic')
tabu_y = f_tabu(inter_k)


sa_time = [
        24.86610010000004,
        4.388360001999899,
        62.76765765900018,
        3.2973416349996114,
        13.479073514001357,
        165.99231116900046
]
sa_time.sort()

f_sa = interp1d(k, sa_time, kind='cubic')
sa_y = f_sa(inter_k)

plt.xlabel("k")
plt.ylabel("vreme u sekundama")


plt.plot(inter_k, scatter_y)
plt.plot(inter_k, greedy_y)
plt.plot(inter_k, berkley_y)
plt.plot(inter_k, tabu_y)
plt.plot(inter_k, sa_y)



plt.legend([ 'scatter', 'greedy', '2app', 'tabu', 'sa'])
plt.show()
