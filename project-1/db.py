                                        ###########################################
                                        #   This file contains database helping   #
                                        #   tools for trading bot.                #
                                        #-----------------------------------------#
                                        #   written by Onur Oduncu                #
                                        #                                         #
                                        ###########################################
import sqlite3 as vt
import pandas as pd

class Sql:
   def __init__(self,dbName:str,username=None,password=None):
      self.dbName = dbName+".db"
      self.__username = username
      self.__password = password


   def engineOpen(self):
      self.__engine = vt.connect('databases/'+self.dbName)
      self.cursor = self.__engine.cursor()
   
   def engineClose(self):
      self.__engine.close()

   def userExist(self,username="",password=""):
      self.engineOpen() 
      self.cursor.execute("select * from users where username=? and password=?",(username,password))
      self.__userlist = self.cursor.fetchall()
      self.engineClose()
      if len(self.__userlist) > 0:
         return True
      else:
         return False     
      

   def getApiInfo(self):
      if self.userExist(self.__username,self.__password):
         self.__apikey = self.__userlist[0][2]
         self.__apisecret = self.__userlist[0][3]
         return (self.__apikey,self.__apisecret)
   
   def createParite(self,parite,interval):
      self.engineOpen() 
      self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {parite+interval} (Time real unique,Open real,High real,Low real,Close real,Volume real,PRIMARY KEY(Time))")
      self.engineClose()

   def createUserLogin(self):
      self.engineOpen() 
      self.cursor.execute("CREATE TABLE IF NOT EXISTS users (username varchar (20),password varchar (20),api_key varchar(64) NOT NULL,api_secret varchar(64) NOT NULL,PRIMARY KEY(username))")
      self.engineClose()

   def insertUserlogin(self,username:str,password:str,api_key:str,api_secret:str):
      self.engineOpen()      
      self.cursor.execute(f"insert into users values(?,?,?,?)",(username,password,api_key,api_secret))
      self.__engine.commit()
      self.engineClose()

   def insertData(self,frame,asset,interval):
      self.engineOpen() 
      for i in frame:        
         self.cursor.execute(f"insert into {asset+interval} select ?,?,?,?,?,? where not exists (select * from {asset+interval} where Time=?)",(i[0]+10800000,i[1],i[2],i[3],i[4],i[5],i[0]))
      self.__engine.commit()
      self.engineClose()

   def getDataSql(self,parite:str,interval:str):
      self.engineOpen()
      self.cursor.execute(f"select * from {parite+interval}")
      self.__allDatas = self.cursor.fetchall()
      self.engineClose()
      return self.__allDatas

   def getLastDataSql(self,parite,interval):
      self.getDataSql(parite,interval)
      return self.__allDatas[len(self.__allDatas)-1]

   def specificTwoDatas(self,parite,interval,x:str,y:str):
      self.engineOpen()
      self.cursor.execute(f"select {x},{y} from {parite+interval}")
      self.__allDatas = self.cursor.fetchall()
      self.engineClose()
      return self.__allDatas
      
      

def Main():
   pass
if __name__ =="__main__":
   Main()