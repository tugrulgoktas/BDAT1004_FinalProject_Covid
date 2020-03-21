import socket
import pandas as pd
import numpy as np
import pyodbc
import urllib
# import urllib.request
# import urllib.parse
# import urllib.error
from sqlalchemy import create_engine
import pymysql
import gviz_api
import openpyxl
# import re
# import ssl
# import requests as req

# resp=req.get("http://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-21.xlsx/redirect-to?url=/")

#getdata from WHO source
#convert data into bytes variable "rawdata"
#borrowed the code to mask python as firefox from https://docs.python.org/3.1/howto/urllib2.html
# user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
# values = {'name' : 'Michael Foord',
#           'location' : 'Northampton',
#           'language' : 'Python' }
# headers = { 'User-Agent' : user_agent }
link = 'http://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-21.xlsx'
df2 = pd.read_excel(link)
print(df2)
# datadl = urllib.parse.urlencode(values)
# req = urllib.request.Request(url,datadl,headers)
# response = urllib.request.urlopen(req)





#they stopped updating this file
#new file that WHO points to
#mysock.connect(('covid.ourworldindata.org', 80))
#cmd = 'GET https://covid.ourworldindata.org/data/new_cases.csv HTTP/1.0\r\n\r\n'.encode()
# rawdata=b''
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('covid.ourworldindata.org', 80))

# mysock.send(cmd)
# while True:
#     data = mysock.recv(512)
#     rawdata = rawdata + data 
#     if len(data) < 1:  
#         break  
# mysock.close()

#convert data to list with header removed
# mydata=rawdata.decode()
# headerpos = mydata.find("\r\n\r\n")

# mydata=mydata[headerpos:]
# test=mydata.splitlines()
# test.pop(0)
# test.pop(0)
# data_list=[]
# for line in test:
#     data_list.append(line.split(','))
  
# #create dataframe from list
# df=pd.DataFrame(data_list)
# print(df)

# #Connect to a SQL Server
# server = 'mysqlerverrr.database.windows.net'
# database = 'BDAT1004W20'
# username = 'azureuser'
# password = 'P@ssw0rd'
# driver= '{ODBC Driver 17 for SQL Server}'
# odbc_str = 'DRIVER='+driver+';SERVER='+server+';PORT=1433;UID='+username+';DATABASE='+ database + ';PWD='+ password
# connect_str = 'mssql+pyodbc:///?odbc_connect=' + urllib.parse.quote_plus(odbc_str)
# engine =create_engine(connect_str)
# print("connection is ok")

# #create SQL Table on Azure server
# df.to_sql('covid', con = engine,if_exists='replace' ,chunksize = 1000)
# print("table created")



