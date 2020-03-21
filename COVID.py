import socket
import pandas as pd
import numpy as np
import pyodbc
import urllib
from sqlalchemy import create_engine
import openpyxl

#connect to the data source and create a dataframe
#change column names to avoid SQL errors later
link = 'http://www.ecdc.europa.eu/sites/default/files/documents/COVID-19-geographic-disbtribution-worldwide-2020-03-21.xlsx'
df = pd.read_excel(link)
df = df.rename(columns={'Countries and territories':'Countries'})

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

