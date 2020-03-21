#this was from when we were going to use the airport code and it can be deleted.

# import urllib.request
# import pandas as pd
# import json

# print('Downloading file...')
# #the following two lines have succesfully downloaded the json file from the URL.
# # url = 'https://datahub.io/core/airport-codes/r/airport-codes.json'
# # urllib.request.urlretrieve(url,"/Users/rober/Dropbox/Georgian W2020/BDAT1004 Data Programming/Final_Assignment/airport_codes.json")

# #These lines convert the json file to a Python List and Panda DataFrame.
# #https://www.mssqltips.com/sqlservertip/5576/importing-json-formatted-data-into-sql-server/
# data = json.load(open("/users/rober/Dropbox/Georgian W2020/BDAT1004 Data Programming/Final_Assignment/airport_codes.json"))
# conversionlist = list()
# for val in data:
#     conversionlist.append(val)
# df_output = pd.DataFrame(data=conversionlist)

# #SQL Database: routledgebdat1004.database.windows.net, routledg, May800520!
# #I paused here as it looks like it would cost $450 to create a database: https://portal.azure.com/?Microsoft_Azure_Education_correlationId=79cfc982-1a1c-41a4-802e-c4202c7e21d3#create/Microsoft.SQLDatabase


# #these test that the download from the URL and the list created work
# print(df_output)
# #print(data)