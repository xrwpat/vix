import pandas as pd
import numpy as np
import os
import datetime
from datetime import datetime
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import ipywidgets as widgets
from IPython.display import display

#% matplotlib nbagg

data=pd.read_csv('big_data_call.csv')

#group all data by stike
group_dict_by_strike_expiry={}
group_by_strike=data[data.type=='C'].groupby(['strike'])

i=0
for strike,strike_groups in group_by_strike:
    print('strike=$',strike)
    print(strike_groups[['days_to_strike','last_bid_price','underlying_close']])

    #####plot 3d scatter
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    #X轴：days_to_strike
    X = strike_groups.days_to_strike
    print(X)
    #Y轴：call_option_last_bid_price
    Y = strike_groups.last_bid_price
    #Z轴: vix_price
    Z = strike_groups.underlying_close


    ax.scatter3D(X, Y, Z, linewidth=0)
    ax.set_xlabel('X:days_to_strike')
    ax.set_ylabel('Y:call_option_last_bid_price')
    ax.set_zlabel('Z:vix_price')
    plt.title('strike='+str(strike))
    plt.show()



