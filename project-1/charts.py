from binance import Client,BinanceSocketManager
import pandas as pd
from db import Sql
import asyncio

class Chart(Sql):
    def __init__(self,dbName:str,username:str,password:str,asset:str,interval="15m",lookback="200d") -> None:
        Sql.__init__(self,dbName,username,password)
        self.__asset = f"{asset.upper()}USDT"
        (self.__Apikey,self.__Apisecret) = self.getApiInfo()
        self.__client = Client(self.__Apikey,self.__Apisecret)
        self.__interval = interval
        self.__lookback = lookback
        self.createParite(self.__asset,self.__interval)
        

    def getminutedata(self,symbol:str,interval:str,lookback:str):
        frame = pd.DataFrame(self.__client.get_historical_klines(symbol, interval, lookback+' ago UTC'))
        frame = frame.iloc[:,:6]
        frame.columns = ['Time','Open','High','Low','Close','Volume']
        self.insertData(list(frame.itertuples(index=False, name=None)),self.__asset)


    def getminutedata(self):
        frame = pd.DataFrame(self.__client.get_historical_klines(self.__asset, self.__interval, self.__lookback+' ago UTC'))
        frame = frame.iloc[:,:6]
        frame.columns = ['Time','Open','High','Low','Close','Volume']
        self.insertData(list(frame.itertuples(index=False, name=None)),self.__asset,self.__interval)

    def mainAssetChart(self,asset:str,interval:str,x:str,y:str):
        self.__assertList = self.specificTwoDatas(asset,interval,x,y)
        frame = pd.DataFrame(self.__assertList,columns=[x,y])
        frame[y] = frame[y].astype(float)
        frame.Time = pd.to_datetime(frame.Time,unit='ms')
        return frame










def main():
    chart = Chart("login","onur","1234","btc")
    


if __name__ == "__main__":
    main()