from sodapy import Socrata
import pandas as pd
client = Socrata("data.cityofnewyork.us", None)
G_2019 = client.get("q5mz-t52e", limit=5000)
G_2018 = client.get("w7fs-fd9i", limit=5000)
G_2017 = client.get("5gj9-2kzx", limit=5000)
#G_2016 = client.get("fw4n-6ehm", limit=1000)
Y_2019 = client.get("2upf-qytp", limit=5000)
#Y_2018 = client.get("yt9m-gskq", limit=1000)
#Y_2017 = client.get("biws-g3hs", limit=5000)
#Y_2016 = client.get("k67s-dv2t", limit=1000)
#FH_2019 = client.get("u6nh-b56h", limit=5000)
#FH_2018 = client.get("am94-epxh", limit=1000)
FH_2017 = client.get("avz8-mqzz", limit=5000)
#FH_2016 = client.get("yini-w76t", limit=1000)

#results_df = pd.DataFrame.from_records(results)

#append lists to the original and print


G_2019.extend(G_2018)
G_2019.extend(G_2017)
#G_2019.extend(G_2016)
#print(G_2019)
'''
Y_2019.extend(Y_2018)
Y_2019.extend(Y_2017)
Y_2019.extend(Y_2016)
print(Y_2019)

FH_2019.extend(FH_2018)
FH_2019.extend(FH_2017)
FH_2019.extend(FH_2016)
print(FH_2019)
'''
import kafka
from kafka import KafkaProducer
from kafka import KafkaClient
import json
import csv

client = KafkaClient("localhost:9092")
producer = KafkaProducer(bootstrap_servers='localhost:9092')
for msg1 in G_2019:
	procuder.send('Green',json.dumps(msg1).encode('utf-8'))

for msg2 in Y_2019:
	procuder.send('Yellow',json.dumps(msg2).encode('utf-8'))

for msg3 in FH_2017:
	producer.send('ForHire',json.dumps(msg3).encode('utf-8'))

from kafka import KafkaConsumer

consumer_green = KafkaConsumer('Green')
consumer_yellow = KafkaConsumer('Yellow')
consumer_FH = KafkaConsumer('ForHire')

#for consumer_Green
xt = pd.DataFrame()
for con_1 in consumer_green:
	x = con_1.value.decode('utf-8')
	x1 = json.loads(x)
	x2 = pd.DataFrame(x1)
	xt = pd.concat([xt,x2])

yt = pd.DataFrame()
for con_2 in consumer_Yellow:
	y = con_2.value.decode('utf-8')
	y1 = json.loads(y)
	y2 = pd.DataFrame(y1)
	yt = pd.concat([yt,y2])

zt = pd.DataFrame()
for con_3 in consumer_FH:
	z = con_3.value.decode('utf-8')
	z1 = json.loads(z)
	z2 = pd.DataFrame(z1)
	zt = pd.concat([zt,z2])

#xt.to_excel('D:/BDBA/SEM_1/Data Engineering/kafka/green.xlsx')
#yt.to_excel('D:/BDBA/SEM_1/Data Engineering/kafka/yellow.xlsx')
#zt.to_excel('D:/BDBA/SEM_1/Data Engineering/kafka/forHire.xlsx')

#convert dataypes of columns here ---------------------

#data type handling and insertion

#xt

xt['dolocationid']=xt['dolocationid'].astype(int)
xt['extra']=xt['extra'].astype(float)
xt['fare_amount']=xt['fare_amount'].astype(float)
xt['improvement_surcharge']=xt['improvement_surcharge'].astype(float)
xt['lpep_dropoff_datetime']=pd.to_datetime(xt['lpep_dropoff_datetime'])
xt['lpep_pickup_datetime']=pd.to_datetime(xt['lpep_pickup_datetime'])
xt['mta_tax']=xt['mta_tax'].astype(float)
xt['passenger_count']=xt['passenger_count'].astype(int)
xt['payment_type']=xt['payment_type'].astype(int)
xt['pulocationid']=xt['pulocationid'].astype(int)
xt['ratecodeid']=xt['ratecodeid'].astype(int)
#xt['store_and_fwd_flag']=xt['store_and_fwd_flag']
xt['tip_amount']=xt['tip_amount'].astype(float)
xt['tolls_amount']=xt['tolls_amount'].astype(float)
xt['total_amount']=xt['total_amount'].astype(float)
xt['trip_distance']=xt['trip_distance'].astype(float)
xt['trip_type']=xt['trip_type'].astype(int)
xt['vendorid']=xt['vendorid'].astype(int)


#yt

yt['dolocationid']=yt['dolocationid'].astype(int)
yt['extra']=yt['extra'].astype(float)
yt['fare_amount']=yt['fare_amount'].astype(float)
yt['improvement_surcharge']=yt['improvement_surcharge'].astype(float)
yt['tpep_dropoff_datetime']=pd.to_datetime(yt['tpep_dropoff_datetime'])
yt['tpep_pickup_datetime']=pd.to_datetime(yt['tpep_pickup_datetime'])
yt['mta_tax']=yt['mta_tax'].astype(float)
yt['passenger_count']=yt['passenger_count'].astype(int)
yt['payment_type']=yt['payment_type'].astype(int)
yt['pulocationid']=yt['pulocationid'].astype(int)
yt['ratecodeid']=yt['ratecodeid'].astype(int)
#yt['store_and_fwd_flag']=yt['store_and_fwd_flag']
yt['tip_amount']=yt['tip_amount'].astype(float)
yt['tolls_amount']=yt['tolls_amount'].astype(float)
yt['total_amount']=yt['total_amount'].astype(float)
yt['trip_distance']=yt['trip_distance'].astype(float)
yt['vendorid']=yt['vendorid'].astype(int)

#zt


#zt['dispatching_base_num']=zt['dispatching_base_num']
zt['dolocationid']=zt['dolocationid'].astype(float)
zt['dropoff_datetime']=pd.to_datetime(zt['dropoff_datetime'])
zt['pickup_datetime']=pd.to_datetime(zt['pickup_datetime'])
zt['pulocationid']=zt['pulocationid'].astype(float)
#zt['sr_flag']=yt['sr_flag']

t2['year'] = pd.DatetimeIndex(t2['tpep_dropoff_datetime']).year
t2['year']  = t2['year'].astype(int)

t1['year'] = pd.DatetimeIndex(t1['lpep_dropoff_datetime']).year
t1['year']  = t1['year'].astype(int)

t3['year'] = pd.DatetimeIndex(t3['dropoff_datetime']).year
t3['year']  = t3['year'].astype(int)
#--------------------------------------

import pymongo
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

db = client.get_database('taxi')


green = db['green']
yellow = db['yellow']
forHire = db['forHire']

green.delete_many({})
yellow.delete_many({})
forHire.delete_many({})

green.insert_many(xt.to_dict('records'))
yellow.insert_many(yt.to_dict('records'))
forHire.insert_many(zt.to_dict('records'))

#user story 1
#1 I want know the price rate comparison between green and yellow taxi

q1 = green.find({'year': 2019},{'total_amount':1,'trip_distance':1})
q2 = yellow.find({'year': 2019},{'total_amount':1,'trip_distance':1})
q3 = pd.DataFrame(q1) #green
q4 = pd.DataFrame(q2) #yellow

#sum of columns in dataframe q3
q5 = q3['total_amount'].sum()
print(q5)
q6 = q3['trip_distance'].sum()
print(q6)

#sum of columns in dataframe q3
q7 = q4['total_amount'].sum()
print(q7)
q8 = q4['trip_distance'].sum()
print(q8)

q9 = q5/q6
print(q9)
q10 = q7/q8
print(q10)

data = {'Taxi Type': ['Green Taxi','Yellow Taxi'],
		'Price Rate': [q9,q10]}
d = pd.DataFrame(data)
print(d)


plot = d.plot.bar(x='Taxi Type',y="Price Rate", rot=0, color = ['g','y'])
print(plot)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')
plot1 = d.plot(kind='bar',x='Taxi Type', y='Price Rate', rot=0,color = ['green','yellow'])
print(plot1)
for hey in plot1:
	print(hey)

'''
plot2 = plt.bar(d.index, d.loc[:,"Price Rate"],width= 0.3, color = ['green','yellow'], label = "Taxi Type")
for hey in plot2:
	print(plot2)
'''
#2 I want to know the different payment methods used in the three years
#3


# to upload data to mongodb atlas---------------------------
client = MongoClient("mongodb+srv://test:test@cluster0-slb5y.mongodb.net/test?retryWrites=true&w=majority")

t1 = pd.read_excel("D:/BDBA/SEM_1/Data Engineering/kafka/t1.xlsx"
                     , header = 0
                     , skipfooter = 1)

t2= pd.read_excel("D:/BDBA/SEM_1/Data Engineering/kafka/t2.xlsx"
                     , header = 0
                     , skipfooter = 1)

t3 = pd.read_excel("D:/BDBA/SEM_1/Data Engineering/kafka/t3.xlsx"
                     , header = 0
                     , skipfooter = 1)

db = client.get_database('taxi')

green = db['green']
yellow = db['yellow']
forHire = db['forHire']

green.insert_many(t1.to_dict('records'))
yellow.insert_many(t2.to_dict('records'))
forHire.insert_many(t3.to_dict('records'))
#-------------------------------------------------------------------