import socket
import pandas as pd
import numpy as np
import pyodbc
import urllib
from sqlalchemy import create_engine
import pymysql
import gviz_api

#getdata from WHO source
#convert data into bytes variable "rawdata"
rawdata=b''
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('covid.ourworldindata.org', 80))
cmd = 'GET https://covid.ourworldindata.org/data/new_cases.csv HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)
while True:
    data = mysock.recv(512)
    rawdata = rawdata + data 
    if len(data) < 1:  
        break  
mysock.close()

#convert data to list with header removed
mydata=rawdata.decode()
headerpos = mydata.find("\r\n\r\n")
mydata=mydata[headerpos:]
test=mydata.splitlines()
test.pop(0)
test.pop(0)
data_list=[]
for line in test:
    data_list.append(line.split(','))
  
#create dataframe from list
df=pd.DataFrame(data_list)
print(df)

#Connect to a SQL Server
server = 'mysqlerverrr.database.windows.net'
database = 'BDAT1004W20'
username = 'azureuser'
password = 'P@ssw0rd'
driver= '{ODBC Driver 17 for SQL Server}'
odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_str)
engine =create_engine(connect_str)
print("connection is ok")

#create SQL Table on Azure server
df.to_sql('covid', con = engine,if_exists='replace' ,chunksize = 1000)
print("table created")



