from binance import Client,BinanceSocketManager
from db import Sql
from time import sleep 
import numpy as np
from datetime import datetime

class Chart(Sql):
    def __init__(self,dbName:str,username:str,password:str) -> None:
        Sql.__init__(self,dbName,username,password)
        (self.__Apikey,self.__Apisecret) = self.getApiInfo()
        self.__client = Client(self.__Apikey,self.__Apisecret)  


    def getminutedata(self,asset:str,interval:str,lookback:str):
        self.createParite(asset,interval)
        frame = np.array(self.__client.get_historical_klines(asset, interval, lookback+' ago UTC'),dtype=float)
        frame = frame[:,:6].copy()
        self.insertData(frame,asset,interval)
        #'Time','Open','High','Low','Close','Volume'

    def mainAssetChart(self,asset:str,interval:str,x:str,y:str):
        self.__assertList = np.array(self.specificTwoDatas(asset,interval,x,y))
        xaxis = np.array([i[0] for i in self.__assertList])
        yaxis = np.array([i[1] for i in self.__assertList])
        if x == "Time":
            xaxis = np.array([datetime.fromtimestamp(i / 1000) for i in xaxis])
        elif y == "Time":
            yaxis = np.array([datetime.fromtimestamp(i / 1000) for i in yaxis])
        return (xaxis,yaxis)
        #datetime.fromtimestamp(i[0] / 1000)
            
    def getRegularData(self,asset:str,interval="15m",lookback="1d"):
        #while True:
        dt_start = datetime.fromtimestamp(self.getLastDataSql(asset,interval)[0] / 1000)
        dt_now = datetime.now()
        #a = (dt_now - dt_start).seconds
        print(dt_start)
        """if a >=15:
                self.getminutedata(asset,interval,str(a)+"m")
            sleep(60)"""
                











def main():
    chart = Chart("login","onur","1234")
    chart.getRegularData("BTCUSDT")
    


if __name__ == "__main__":
    main()