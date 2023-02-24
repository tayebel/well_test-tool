import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import pandas as pd
import numpy as np
import matplotlib as mpl
import os


mpl.use('TkAgg')

plt.style.use('dark_background')



def plot_graphs(data, columns,data2,columns2,df):
    i = 0
    l = 1
    fig, ax = plt.subplots(1, 1, figsize=(16, 9))
    ax.set_ylim(0.001, 10)
    ax.set_xlim(0.0001, 1000)
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_title('Fetkovich - SPE 13169 WVG Well A ', fontsize=14, fontweight='bold')
    ax.set_xlabel('tDd', fontsize=16, fontweight='bold')
    ax.set_ylabel('qDd', fontsize=16, fontweight='bold')
    colors = plt.rcParams['axes.prop_cycle'].by_key()['color']
    color_index = 0
    
    while i < len(columns):
        rerw = np.asarray(data.iloc[:, [i, i + 1]])
        rerw = rerw[~np.isnan(rerw).any(axis=1)]
        t=rerw[:, 0]
        q=rerw[:, 1]
        ax.plot(t, q, linestyle='solid', c=colors[color_index])
        color_index = (color_index + 1) % len(colors)
        i += 2
    while l< len(columns2):
        data2.to_numpy()
        d=np.asarray(data2.iloc[:, [0, l]])
        d=d[~np.isnan(d).any(axis=1)]
        t1=d[:, 0]
        q1=d[:, 1]
        ax.plot(t1, q1, linestyle='solid', c=colors[color_index])
        color_index = (color_index + 1) % len(colors)
        l+=1 
    
    
    df.to_numpy()

    wvgwa = np.asarray(df.iloc[:, [0, 1]])
    wvgwa = wvgwa[~np.isnan(wvgwa).any(axis=1)]
    x = wvgwa[:, 0]
    y = wvgwa[:, 1]

    ax2 = ax.twinx().twiny()
    ax2.set_yscale('log')
    ax2.set_xscale('log')
    ax2.set_ylim(1, 10000)
    ax2.set_xlim(1, 10000000)
    # turn Twin Axis labels off
    ax2.set_xticklabels([])
    ax2.set_yticklabels([])
    ax2.tick_params(which='both', direction='in', color='white', width=1, length=5)
    gmdl = ax2.scatter(x, y, s=10, facecolors='none', edgecolors='r')

    plt.show()





path = os.getcwd()
file_name1='Fetko-tranTCdata.csv'
path1=os.path.join(path,file_name1)

file_name2='Fetko-depTCdata.csv'
path2=os.path.join(path,file_name2)

file_name3='WVGWA_SPE13169.csv'
path3=os.path.join(path,file_name3)

data = pd.read_csv(path1, dtype=float)
data2 = pd.read_csv(path2, dtype=float)



columns = data.columns
columns2 = data2.columns
df = pd.read_csv(path3, dtype=float)
plot_graphs(data,columns,data2,columns2,df)

