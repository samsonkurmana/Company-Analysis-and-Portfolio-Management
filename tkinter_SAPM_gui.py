import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu


import numpy as np
import pandas as pd
import pandas_datareader.data as web
from pandas_datareader import data
import matplotlib.pyplot as plt
from tkinter import *
from tkinter.ttk import *
from tkinter import font
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandastable import Table, TableModel
#from pandastable import TableCanvas

import json
import requests

import pandas_ta as ta

from plotly.offline import plot
import plotly.graph_objs as go
from mpl_finance import candlestick_ohlc
import datetime as dt
import matplotlib.dates as mdates







win = tk.Tk()


win.title("SAPM Project")


win.geometry('1000x1000')



#==================================================
# Tabs:

#scrollbar = Scrollbar(win)
#scrollbar. pack( side = RIGHT, fill=Y )

tabControl = ttk.Notebook(win)         
tab1 = ttk.Frame(tabControl)           
tabControl.add(tab1, text='Modern Portfolio Theory')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Company Analysis and Metrics')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Fundamental Indicators')



tabControl.pack(expand= 1, fill="both") 



mighty= ttk.LabelFrame(tab1, text= ' Security Analysis and Portfolio Management')
mighty.grid(column=0, row=0, padx=8, pady=14) 


mighty1=ttk.LabelFrame(tab1, text= 'Most Active stocks')
mighty1.grid(column=3, row=0, padx=8, pady=14)  


mighty2= ttk.LabelFrame(tab2, text= ' Stock Analysis')
mighty2.grid(column=0, row=0, padx=8, pady=14) 


mighty3= ttk.LabelFrame(tab2, text= ' Company profile')
mighty3.grid(column=0, row=15, padx=8, pady=1) 

#mighty4= ttk.LabelFrame(tab2, text= 'income Analysis')
#mighty4.grid(column=0, row=30, padx=8, pady=14) 

mighty5=ttk.LabelFrame(tab2, text= ' company metrics')
mighty5.grid(column=2, row=15, padx=8, pady=14) 


mighty6=ttk.LabelFrame(tab3, text= ' income analysis')
mighty6.grid(column=0, row=0, padx=8, pady=4) 
 
mighty7=ttk.LabelFrame(tab3, text= ' cashflow')
mighty7.grid(column=2, row=0, padx=8, pady=4) 

#==================================================
#Events:

def _quit():      
    win.quit()
    win.destroy()
    exit()


def click_me():
    t11= name.get()
    def cash_flow(Name):
       url= ('https://financialmodelingprep.com/api/v3/financials/cash-flow-statement/'+Name+'')
       
       res = requests.get(url)
       dt = res.json()
       bs=dt['financials']
       bs=bs[0]
       pt = Table(mighty7)
       incomeinitial=pd.DataFrame(list(bs.items()),columns=['item','value'])
       df = pt.model.df
       table = pt = Table(mighty7, dataframe=incomeinitial,
                                showtoolbar=True, showstatusbar=False)
       table.show()
       
       
    oo=cash_flow(t11)    
    lb1 = Label(mighty7, text=oo)
    lb1.grid(column=2, row=0, sticky=W)
#    
    def company_profile(Name):
        #rates = []
        url = ('https://financialmodelingprep.com/api/v3/company/profile/'+Name+'')
        #url = ('https://financialmodelingprep.com/api/v3/company/profile/'+Name+'')
        #url = ('https://fmpcloud.io/api/v3/profile/'+Name+'?apikey=33425fa333b6d1a12aa0c76bac6336c7')
        res = requests.get(url)
        dat = res.json()
        #print(dat)
        #bs=(json.dumps(data, sort_keys=True, indent=4))
        #bs = pd.DataFrame.from_dict(data)
       # bs = bs.T
       
        bs=dat['profile']
        pt = Table(mighty3)
        incomeinitial=pd.DataFrame(list(bs.items()),columns=['item','value'])
        df = pt.model.df
        table = pt = Table(mighty3, dataframe=incomeinitial,
                                showtoolbar=True, showstatusbar=False)
        table.show()
       
       
       
#    
    
    
    
    
        
    cp=company_profile(t11)   
    lb2 = Label(mighty3, text=cp)
    lb2.grid(column=0, row=3, sticky=W)
    
    def income_statement(Name):
        url=('https://financialmodelingprep.com/api/v3/financials/income-statement/'+Name+'')
        res = requests.get(url)
        data = res.json()
        bs=data['financials']
        #bs=bs[0]
        #bs=daa['financials']
        bs=bs[0]
        pt = Table(mighty6)
        incomeinitial=pd.DataFrame(list(bs.items()),columns=['item','value'])
        df = pt.model.df
        table = pt = Table(mighty6, dataframe=incomeinitial,
                                showtoolbar=True, showstatusbar=False)
        table.show()
       
        
    income=income_statement(t11)   
    lb3 = Label(mighty6, text=income)
    lb3.grid(column=0, row=0, sticky=W)


    def company_ratios(Name):
        url = ('https://financialmodelingprep.com/api/v3/financial-ratios/'+Name+'')
        res = requests.get(url)
        data = res.json()
        
        #print(data['ratios'][0])
        valuation=data['ratios'][0]['investmentValuationRatios']
        profitabilityIndicatorRatios=data['ratios'][0]['profitabilityIndicatorRatios']
        operatingPerformanceRatios=data['ratios'][0]['operatingPerformanceRatios']
        liquidityMeasurementRatios=data['ratios'][0]['liquidityMeasurementRatios']
        debtRatios=data['ratios'][0]['debtRatios']
        cashFlowIndicatorRatios=data['ratios'][0]['cashFlowIndicatorRatios']
             
        pt = Table(mighty5)
        
        
        valuation=pd.DataFrame(list(valuation.items()),columns=['Ratio',Name])
        profitabilityIndicatorRatios=pd.DataFrame(list(profitabilityIndicatorRatios.items()),columns=['Ratio',Name])
        operatingPerformanceRatios=pd.DataFrame(list(operatingPerformanceRatios.items()),columns=['Ratio',Name])
        liquidityMeasurementRatios=pd.DataFrame(list(liquidityMeasurementRatios.items()),columns=['Ratio',Name])
        debtRatios=pd.DataFrame(list(debtRatios.items()),columns=['Ratio',Name])
        cashFlowIndicatorRatios=pd.DataFrame(list(cashFlowIndicatorRatios.items()),columns=['Ratio',Name])
        
        fr=[valuation,profitabilityIndicatorRatios,operatingPerformanceRatios,liquidityMeasurementRatios,debtRatios,cashFlowIndicatorRatios]
        cfr=pd.concat(fr)
        
        df = pt.model.df
        table = pt = Table(mighty5, dataframe=cfr,
                                    showtoolbar=True, showstatusbar=False)
        table.show()


    crat=company_ratios(t11)   
    lb3 = Label(mighty5, text=crat)
    lb3.grid(column=1, row=15, sticky=W)








####################################################
    
    def historical_price(Name):
        url=('https://financialmodelingprep.com/api/v3/historical-price-full/'+Name+'')
        res = requests.get(url)
        
        data = res.json()
        data=data['historical'][-120:]
        bs = pd.DataFrame.from_dict(data)
        bs.set_index('date', inplace=True)
       # print(bs.keys)
        
        #bs['close'].plot()
    
        
        def cscheme(colors):
            aliases = {
                'BkBu': ['black', 'blue'],
                'gr': ['green', 'red'],
                'grays': ['silver', 'gray'],
                'mas': ['black', 'green', 'orange', 'red'],
            }
            aliases['default'] = aliases['gr']
            return aliases[colors]
        
        last_ = bs.shape[0]
        price_size=(8, 6) 
        
        def machart(kind, fast, medium, slow, append=True, last=last_, figsize=price_size, colors=cscheme('mas')):
            
            title = kind
            ma1 = bs.ta(kind=kind, length=fast, append=append)
            ma2 = bs.ta(kind=kind, length=medium, append=append)
            ma3 = bs.ta(kind=kind, length=slow, append=append)
            
            #figure1 = plt.Figure(figsize=(6,5), dpi=100)
            #ax1 = figure1.add_subplot(111)
            #bar1 = FigureCanvasTkAgg(figure1, tab3)
            #bar1.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            madf = pd.concat([bs['close'], bs[[ma1.name, ma2.name, ma3.name]]], axis=1, sort=False).tail(last)
            madf.plot(figsize=figsize, title=title, color=colors, grid=True) 
            #ax1.set_title('MACD')
    
        def rsi_plot(bs):
    
            window_length=14
            close = bs['close']
            # Get the difference in price from previous step
            delta = close.diff()
            # Get rid of the first row, which is NaN since it did not have a previous 
            # row to calculate the differences
            delta = delta[1:] 
            
            # Make the positive gains (up) and negative gains (down) Series
            up, down = delta.copy(), delta.copy()
            up[up < 0] = 0
            down[down > 0] = 0
            
            # Calculate the EWMA
            roll_up1 = up.ewm(span=window_length).mean()
            roll_down1 = down.abs().ewm(span=window_length).mean()
            
            # Calculate the RSI based on EWMA
    #        RS1 = roll_up1 / roll_down1
    #        RSI1 = 100.0 - (100.0 / (1.0 + RS1))
            
            # Calculate the SMA
            roll_up2 = up.rolling(window_length).mean()
            roll_down2 = down.abs().rolling(window_length).mean()
            
            # Calculate the RSI based on SMA
            RS2 = roll_up2 / roll_down2
            RSI2 = 100.0 - (100.0 / (1.0 + RS2))
            
            # Compare graphically
            plt.figure(figsize=(8, 6))
#            figure2 = plt.Figure(figsize=(6,5), dpi=100)
#            ax2 = figure2.add_subplot(111)
#            bar2 = FigureCanvasTkAgg(figure2, tab3)
#            bar2.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
            #RSI1.plot()
            
            RSI2.plot()
            plt.legend(['RSI via SMA'])
            plt.axhline(y=30,     color='red',   linestyle='-')
            plt.axhline(y=70,     color='blue',  linestyle='-')
            plt.show()
            #ax2.set_title('RSI')
        def macd(bs):        
            recent=120
            ind_size = (8, 6)
            macddf = bs.ta.macd(fast=8, slow=21, signal=9, min_periods=None, append=True)
            print(macddf)
            
            macddf[[macddf.columns[0], macddf.columns[2]]].tail(recent).plot(figsize=(16, 2), color=cscheme('BkBu'), linewidth=1.3)
           
            macddf[macddf.columns[1]].tail(recent).plot.area(figsize=ind_size, stacked=False, color=['silver'], linewidth=1, title="macd", grid=True).axhline(y=0, color="black", lw=1.1)
    
        def aroon(bs):
            arn=ta.aroon(bs['close'],length=None,offset=None)
            
            arn.plot()
        
        def bol_band(bs):
            b=ta.bbands(bs['close'], length=None, std=None, mamode=None, offset=None)
            bs['close'].plot()
            b=pd.concat([bs['close'],b['BBL_20'],b['BBM_20'],b['BBU_20']], axis=1, sort=False)
            
            b.plot()
            
        def stochos(bs):
            b=ta.stoch(bs['high'],bs['low'],bs['close'],fast_k=None, slow_k=None, slow_d=None, offset=None)
            
            b.plot()
    
        def chmf(bs):
            b=ta.cmf(bs['high'],bs['low'],bs['close'],bs['volume'],bs['open'],length=None, offset=None)
            
            b.plot()
     
        def cdlp(bs):
            bs = bs[['open', 'high', 'low', 'close']]
            bs.reset_index(level=0, inplace=True) 
            #print(bs)
            bs['date'] = bs['date'].map(mdates.datestr2num)
           # df['Date'] = df['Date'].map(mdates.date2num)
            
            ax = plt.subplot()
            candlestick_ohlc(ax,bs.values, width=5, colorup='g', colordown='r')
            ax.xaxis_date()
            ax.grid(True)
            
            plt.show()
        plt.subplots(3,3) 
        
        rsi_plot(bs)
        machart('ema', 8, 21, 50, last=120)
        machart('sma',8, 21, 50, last=120)
        macd(bs)
        aroon(bs)
        bol_band(bs)   
        stochos(bs)
        chmf(bs)
        cdlp(bs)    
         
    oust=historical_price(t11)      
    lb88 = Label(mighty6, text=oust)
    lb88.grid(column=0, row=2, sticky=W)





















menu_bar= Menu(win)

win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)        #tearoff:
file_menu.add_command(label='New')
#file_menu.add_separator()                   #Seperator-
file_menu.add_command(label='Exit', command=_quit)
menu_bar.add_cascade(label='File', menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)      
menu_bar.add_cascade(label='Help', menu=help_menu)
help_menu.add_command(label='About')
#==================================================

#Label 
a_label = ttk.Label(mighty2, text= "Enter a Name:")
a_label.grid(column =0, row=0)
#

##Textbox 
name = tk.StringVar()
name_entered = ttk.Entry(mighty2, width=12, textvariable=name)
name_entered.grid(column= 0, row=1, sticky=tk.W)
name_entered.focus() 
#
##Button 
action=ttk.Button(mighty2,text= "Click", command=click_me)
action.grid(column =2, row =1)

frame1=Frame(mighty)
frame2=Frame(mighty1)

lbl0=Label(frame1, text="Modern Portfolio Theory",font=('Monotype Corsiva',20))
lbl0.grid(column=1, row=0, sticky=W)
lbl11 = Label(frame1, text="Stock 1",font=('Comic Sans MS',15))
lbl11.grid(column=0, row=1, sticky=W)
txt11 = Entry(frame1,width=14)
txt11.grid(column=1, row=1, sticky=W)
lbl12 = Label(frame1, text="Stock 2",font=('Comic Sans MS',15))
lbl12.grid(column=0, row=2, sticky=W)
txt12 = Entry(frame1,width=14)
txt12.grid(column=1, row=2, sticky=W)
lbl13 = Label(frame1, text="Stock 3",font=('Comic Sans MS',15))
lbl13.grid(column=0, row=3, sticky=W)
txt13 = Entry(frame1,width=14)
txt13.grid(column=1, row=3, sticky=W)
lbl14 = Label(frame1, text="Stock 4",font=('Comic Sans MS',15))
lbl14.grid(column=0, row=4, sticky=W)
txt14 = Entry(frame1,width=14)
txt14.grid(column=1, row=4, sticky=W)

lbl15 = Label(frame1, text="Stock 5",font=('Comic Sans MS',15))
lbl15.grid(column=0, row=5, sticky=W)
txt15 = Entry(frame1,width=14)
txt15.grid(column=1, row=5, sticky=W)

lbl16 = Label(frame1, text="Stock 6",font=('Comic Sans MS',15))
lbl16.grid(column=0, row=6, sticky=W)
txt16 = Entry(frame1,width=14)
txt16.grid(column=1, row=6, sticky=W)

#
lb17 = Label(frame1, text="Start Date(DD-MM-YYYY)",font=('Comic Sans MS',15))
lb17.grid(column=0, row=7, sticky=W)
txt17 = Entry(frame1,width=14)
txt17.grid(column=1, row=7, sticky=W)


lb18 = Label(frame1, text="End Date(DD-MM-YYYY)",font=('Comic Sans MS',15))
lb18.grid(column=0, row=8, sticky=W)
txt18 = Entry(frame1,width=14)
txt18.grid(column=1, row=8, sticky=W)



def active_stocks():
    url=("https://financialmodelingprep.com/api/v3/stock/actives")
    res = requests.get(url)

    data = res.json()
    data=data['mostActiveStock']
#    bs = pd.DataFrame.from_dict(data)
#    bs.index = np.arange(1,len(bs)+1)
    pt = Table(mighty1)
#    #print(pt)
    actv=pd.DataFrame(data,columns=['ticker','changes','price','changesPercentage','companyName'])
    
    df = pt.model.df
    table = pt = Table(mighty1, dataframe=actv,
                                showtoolbar=False, showstatusbar=False)
   # print(data)
    table.autoResizeColumns()
    table.show()
   # print(table)   
        
ac=active_stocks()  
txt108 = Label(mighty1,text=ac,font=('Comic Sans MS',20))
txt108.grid(column=0, row=0, sticky=W)





def clicked():
    s11= txt11.get()
    s12= txt12.get()
    s13= txt13.get()
    s14= txt14.get()
    s15= txt15.get()
    s16= txt16.get()
    s17= txt17.get()
    s18= txt18.get()
#list of stocks in portfolio
    stocks = [txt11.get(),txt12.get(),txt13.get(),txt14.get(),txt15.get(),txt16.get()]
 
##download daily price data for each of the stocks in the portfolio
    data = web.DataReader(stocks,data_source='yahoo',start=txt17.get(),end=txt18.get())['Adj Close']
#
    data.sort_index(inplace=True)
    #data.to_csv("home.csv")
    table=data
    figure = Figure(figsize=(6,5), dpi=100)
    table.plot(kind='line')
    canvas = FigureCanvasTkAgg(figure,tab1)



# calculate daily and annual returns of the stocks
    returns_daily = table.pct_change()
    import seaborn as sns
    sns.pairplot(returns_daily[1:])
    returns_annual = returns_daily.mean() * 250
    lbl8_1 = Label(mighty, text='Annual returns of each stock ')
    lbl8_1.grid(column=0, row=9, sticky=W)
    lbl8_1 = Label(mighty, text=returns_annual)
    lbl8_1.grid(column=0, row=10, sticky=W)
    # get daily and covariance of returns of the stock
    cov_daily = returns_daily.cov()
    cov_annual = cov_daily * 250
    
    port_returns = []
    port_volatility = []
    stock_weights = []
    sharpe_ratio = []
    
    # set the number of combinations for imaginary portfolios
    num_assets = len(stocks)
    num_portfolios = 50000
    
    # populate the empty lists with each portfolios returns,risk and weights
    for single_portfolio in range(num_portfolios):
        weights = np.random.random(num_assets)
        weights /= np.sum(weights)
        returns = np.dot(weights, returns_annual)
        volatility = np.sqrt(np.dot(weights.T, np.dot(cov_annual, weights)))
        sharpe = returns/volatility
        sharpe_ratio.append(sharpe)
        port_returns.append(returns)
        port_volatility.append(volatility)
        stock_weights.append(weights)
    
    # a dictionary for Returns and Risk values of each portfolio
    portfolio = {'Returns': port_returns,
                 'Volatility': port_volatility,
                 'sharpe Ratio': sharpe_ratio}
    
    # extend original dictionary to accomodate each ticker and weight in the portfolio
    for counter,symbol in enumerate(stocks):
        portfolio[symbol+' Weight'] = [Weight[counter] for Weight in stock_weights]
    
    # make a nice dataframe of the extended dictionary
    df = pd.DataFrame(portfolio)
    
    # get better labels for desired arrangement of columns
    column_order = ['Returns', 'Volatility', 'sharpe Ratio'] + [stock+' Weight' for stock in stocks]
    
    # reorder dataframe columns
    df = df[column_order]
    
    #print(df.head())
    max_sharpe_port = df.iloc[df['sharpe Ratio'].idxmax()]
    max_sharpe_port
    
    #locate positon of portfolio with minimum  standard deviation
    min_vol_port = df.iloc[df['Volatility'].idxmin()]
    #print(min_vol_port)
    lbl9_1 = Label(mighty, text='Minimum Variance Portfolio')
    lbl9_1.grid(column=0, row=12, sticky=W)
    lbl9_2 = Label(mighty, text='Maximum Sharpe Portfolio')
    lbl9_2.grid(column=1, row=12, sticky=W)
    lbl9_1 = Label(mighty, text=min_vol_port)
    lbl9_1.grid(column=0, row=13, sticky=W)
    lbl9_2= Label(mighty, text=max_sharpe_port)
    lbl9_2.grid(column=1, row=13, sticky=W)
   
    
    

  
    
   
   
    figure1 = Figure(figsize=(6,5), dpi=100)
    ax1 = figure1.add_subplot(111)
    bar1 = FigureCanvasTkAgg(figure1, tab1)
    plt.style.use('seaborn-dark')
    df.plot.scatter(x='Volatility', y='Returns', c='sharpe Ratio',
                    cmap='RdYlGn', edgecolors='black', figsize=(10, 8), grid=True)
    plt.xlabel('Volatility (Std. Deviation)')
    plt.ylabel('Expected Returns')
    plt.title('Efficient Frontier')
    plt.scatter(max_sharpe_port[1],max_sharpe_port[0],marker=(5,1,0),color='r',s=500)
    plt.scatter(min_vol_port[1],min_vol_port[0],marker=(5,1,0),color='g',s=500)
    
    canvas = FigureCanvasTkAgg(figure1,tab1)
    canvas.draw()
   

    #return figure1
Button(frame1, text='Submit' ,command=clicked).grid(row=15, column=1, sticky=W)
frame1.grid(row=3,column=0)


#===============================================================================
#Start GUI
win.mainloop()