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

i=1

fig=plt.figure()
color=['grey','red','blue','yellow','green']

for strike,strike_groups in group_by_strike:
    print('strike=$',strike)
    #pick up data with days to strike less than 30
    data_select=strike_groups[strike_groups.days_to_strike<30]\
        [['quote_date','days_to_strike','last_ask_price','last_bid_price','underlying_close']]
    #pick up data with date between 2008,8,20 to 2008,10,23
    data_select=data_select[pd.to_datetime(data_select.quote_date)>datetime(2008,8,20)]
    data_select = data_select[pd.to_datetime(data_select.quote_date)< datetime(2008, 10, 23)]
    #pn is mid option price between bid and ask
    data_select['p']=(data_select.last_ask_price+data_select.last_bid_price)/2
    #p0 is the option price under the lowest vix(underlying assets)
    p0=data_select[data_select.underlying_close==np.min(data_select.underlying_close)]['p']
    data_select['p0']=[p0]*len(data_select)
    #return_rate=pn/p0
    data_select['return_rate']=data_select.p/data_select.p0
    print(data_select[['return_rate','p','p0']].head())

    ###plot 2d scatter
    #draw relationship between return rate and vix price
    # fig1= plt.figure()
    # ax = fig.gca()
    # #X轴：vix_price
    # X = data_select.underlying_close
    # #Y轴：return_rate
    # Y = data_select.return_rate
    # ax.scatter(X, Y, linewidth=0)
    # ax.set_xlabel('X:vix_price')
    # ax.set_ylabel('Y:return_rate')
    # plt.title('2008-8-20 to 2008-10-23:'+'strike='+str(strike)+',days to strike under 1 month')
    # plt.show()

    ##



    # X轴：vix_price
    X = data_select.underlying_close
    # Y轴：return_rate
    Y = data_select.return_rate
    if len(X)>0:
        plt.scatter(X, Y, linewidth=0, color=color[i-1],s=20+25*i,label='strike='+str(strike))
        print(Y)
        i=i+1

    if i % 5==0:
        plt.legend()  # 显示图例
        plt.savefig('2008-8-20 to 2008-10-23:days to strike under 1 month'+str(strike)+'.png')
        plt.show()
        i=0
        X=0
        Y=0
    else:
        continue
    # plt.title('2008-8-20 to 2008-10-23:'+'days to strike under 1 month')




# ############################
#     #####plot 3d scatter
#     fig2 = plt.figure()
#     ax = fig.gca(projection='3d')
#     #X轴：days_to_strike
#     X = strike_groups.days_to_strike
#     print(X)
#     #Y轴：call_option_last_bid_price
#     Y = strike_groups.last_bid_price
#     #Z轴: vix_price
#     Z = strike_groups.underlying_close
#
#
#     ax.scatter3D(X, Y, Z, linewidth=0)
#     ax.set_xlabel('X:days_to_strike')
#     ax.set_ylabel('Y:call_option_last_bid_price')
#     ax.set_zlabel('Z:vix_price')
#     plt.title('strike='+str(strike))
#     plt.show()





