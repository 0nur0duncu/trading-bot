import sqlite3 as db

class DB:
    def __init__(self,dbName:str,loc ="databases/") -> None:
        self.__dbName = dbName
        self.__loc = loc
        self.__engine = db.connect(loc+dbName+'.db')
        self.__cursor = self.__engine.cursor()
        self.__tables = list()
        self.__cursor.execute("SELECT name FROM sqlite_schema")
        for i in self.__cursor.fetchall():
            if "sqlite_" not in i[0] and i[0] not in self.__tables:
                self.__tables.append(i[0])


    def getDBname(self) -> str:
        return self.__dbName

    def getloc(self) -> str:
        return self.__loc

    def getEngine(self):
        return self.__engine

    def createTable(self,tableName:str,*params):
        text = "CREATE TABLE IF NOT EXISTS {} (".format(tableName)
        for i in range(0,int(len(params)),2):
            text += str(params[i]) +" varchar ("+str(params[i+1])+") NOT NULL,"
        text += "PRIMARY KEY({}))".format(params[0])
        self.__commit(text)


    def insertData(self,tableName:str,*params):
        if tableName in self.__tables:
            text = "insert into {} values(".format(tableName)
            for i in range(len(params)):
                text +="?"
                if len(params) == i+1:
                    text +=")"
                else:
                    text +=","
            self.__commit(text,params)
        else:
            print("invalid table name")
        
        
    def __commit(self,text:str,params = False):
        if params:
            self.__cursor.execute(text,params)
        else:
            self.__cursor.execute(text)
        self.__engine.commit()
        self.__cursor.execute("SELECT name FROM sqlite_schema")
        for i in self.__cursor.fetchall():
            if "sqlite_" not in i[0] and i[0] not in self.__tables:
                self.__tables.append(i[0])
    

    
        






def Main():
    sql = DB("onur")
    sql.insertData("USER","ali","veli","mert")
    sql.getEngine().close()
    pass


if __name__ == "__main__":
    Main()