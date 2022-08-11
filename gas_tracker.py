from datetime import datetime, timedelta
from brownie import *
import plotext as plt
import time

network.connect('arbitrum-main')

graph_width = timedelta(days=1).total_seconds()
points_x_count = 24*60*60
sleep_time = graph_width/points_x_count

plt.title(network.show_active() + " gas history for last 24 hours")
plt.ylabel("Gas price")

x = []
y = []

while True:    
    plt.clear_terminal()
    plt.clear_data()    
    #plt.plot_size(width=plt.terminal_width(), height=plt.terminal_height())    

    date_time = int(datetime.now().timestamp())
    gas_price = float(web3.fromWei(web3.eth.gasPrice, 'gwei'))
        
    x.append(date_time)    
    y.append(gas_price)

    if len(x) > points_x_count:
        x.pop(0)
        y.pop(0)
        
    xticks = [x[0] + timedelta(hours=i).total_seconds() for i in range(25)]    
    xlabels = [datetime.fromtimestamp(tick).strftime("%H:%M") for tick in xticks]    
    plt.xticks(xticks, xlabels)

    # setting xlabel to current day
    plt.xlabel("Starting date " + datetime.fromtimestamp(x[0]).strftime("%d/%m/%Y"))
    # setting x axis limit to first element timestamp + 1 day
    plt.xlim(x[0], x[0] + timedelta(days=1).total_seconds())
    # setting y axis limit to 110% of max value
    plt.ylim(0, float(max(y))*1.1) 
    plt.plot(x, y)        
    plt.show()
    
    time.sleep(sleep_time)