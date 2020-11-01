import pandas as pd
import xlrd

# insert the excel data into a dataframe
data = pd.read_excel("path to data file"
                     ,sheet_name='final'
                     ,skiprows=1
                     , header = 0
                     , skipfooter = 1)

#print(data)
concat = lambda x : str(x.CaseID) + "_" + str(x.Date)+"_"+ str(x.City).replace(' ','_')
a = data.apply(concat,axis=1)
#print(a)
#print(data.dtypes)
b = data.assign(new_cityID=a.values)
#print(b)

Cities_df = b.filter(['new_cityID'
                                , 'City'
                                  ,'Date'
                                  , 'CityPopulation'
                                  , 'UrbanPopulation(%of total population)'
                                  , 'Density(persons/km2)'
                                  , 'WasteGenerationrate(kg/person/day)'
                                  , 'Avg GDP(US$/person/year)'
                                  , 'CO2emission(capita)'
                                  , 'Ecologicalfootprint(gha/capita)'
                                  , 'LifeExpectancyboth(years)'
                                  , 'AdultMortalityrate(probability of dying between the ages of 15 and 60 per 1000 adults)'], axis = 1)
#print(Cities_df)


Waste_management_df = b.filter(['new_cityID'
                                  ,'Date'
                                  ,'Extend of plastic waste separation at the municipality level'
                                  , 'Extend of paper waste separation at the municipality level'
                                  , 'Extend of metal waste separation at the municipality level'
                                  , 'Extend of glass waste separation at the municipality level'
                                  , 'Extend of organic waste separation at the municipality level'
                                  , 'Extend of battery separation at the municipality level'
                                  , 'Extend of medical waste separation at the healthcare centers'
                                  , 'Extend of electric and electronic waste separation at the municipality level'
                                  , 'Extend of waste dispersed in the city'
                                  , 'Extend of waste separation at the house level'
                                  , 'Extend of waste separation at the business level'
                                  , 'Hazardous waste being treated'], axis = 1)

#print(Waste_management_df)


Solid_waste_df = b.filter(['new_cityID'
                           ,'Date'
                           , 'Total Waste generated(KG)'
                               , 'food & organic waste'
                               , 'Metal Waste'
                               , 'Glass Waste'
                               , 'Other Waste'
                               , 'Paper Cardboard Waste'
                               , 'Plastic Waste'
                               , 'Rubber & Leather Waste'
                               , 'Wood Waste'
                               , 'Yard and Garden Green Waste'], axis = 1)

#print(Solid_waste_df)


import pymongo
#import dns
from pymongo import MongoClient
import csv

#the below LOC connects python to mongodb atlas
client = MongoClient('mongodb://localhost:27017/')

db = client.get_database('WasteManagement')

solid_waste = db['Solid_waste_df']
waste_management = db['Waste_management_df']
cities = db['Cities_df']

# solid_waste.delete_many({})
# waste_management.delete_many({})
# cities.delete_many({})

#sample insert in mongodb cluster
#new_rec = {'name':'Ashton'}

# solid_waste.insert_many(Solid_waste_df.to_dict('records'))
# waste_management.insert_many(Waste_management_df.to_dict('records'))
# cities.insert_many(Cities_df.to_dict('records'))

#Below are the queries

#1. Mongo Query
#-----------------------------------------------------------------

query1 = {"$or":[{"Extend of waste dispersed in the city" : {"$lt":3}},{"Hazardous waste being treated" : {"$lt":3}}]}
								
query2 = {"new_cityID":1}

query3 = waste_management.find(query1,query2)
query3_df = pd.DataFrame(query3)
#for index,row in query3_df.iterrows():
#    print(row)
query7 = pd.DataFrame()
query4 = {"City":1}
for index,row in query3_df.iterrows():
    query5 = row["new_cityID"]
    query6 = cities.find({"new_cityID":query5},query4)
    #print(list(query6))
    query6 = pd.DataFrame(query6)
    query7 = pd.concat([query6,query7])
#print(query7)
#drop the id column in the dataframe
query7 = query7.drop(['_id'],axis=1)
print(query7)


#---------------------with user input----------------------------------------------
city_name = ""
while city_name != "quit":
    city_name = input('Enter the name of the city:')
    q1 = cities.find({"City":city_name},{"new_cityID":1})
    df_q1 = pd.DataFrame(q1)
    for index,row in df_q1.iterrows():
        q2 = row["new_cityID"]
        q3 = waste_management.find({"new_cityID":q2},{"waste dispersed":1})
        df_q3 = pd.DataFrame(q3)
        #print(df_q3)
        q4 = df_q3.drop(['_id'],axis=1)
        #print(q4)
        q5 = q4["waste dispersed"].values[0]
        print(q5)
        if q5<=3:
            print(city_name, "What a shame!!, you have to manage your waste for the betterment of the environment")
        else:
            print(city_name," you're doing good in terms of waste management. Keep it up!!")
            
#--------------------------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

city_name = ""
while city_name != "quit":
    city_name = input('Enter the name of the city:')
    if city_name == "quit":
        break
    else:
        q1 = cities.find({"City":city_name},{"new_cityID":1})
        df_q1 = pd.DataFrame(q1)
        df_temp = pd.DataFrame()
        for index,row in df_q1.iterrows():
            q2 = row["new_cityID"]
            q3 = waste_management.find({"new_cityID":q2},{"Date":1
                                                            ,"Extend of waste dispersed in the city":1 
                                                            ,"Hazardous waste being treated":1
                                                            ,"Extend of plastic waste separation at the municipality level":1
                                                            ,"Extend of paper waste separation at the municipality level":1
                                                            ,"Extend of metal waste separation at the municipality level":1
                                                            ,"Extend of glass waste separation at the municipality level":1
                                                            ,"Extend of organic waste separation at the municipality level":1
                                                            ,"Extend of battery separation at the municipality level":1
                                                            ,"Extend of medical waste separation at the healthcare centers":1
                                                            ,"Extend of electric and electronic waste separation at the municipality level":1
                                                            ,"Extend of waste separation at the house level":1
                                                            ,"Extend of waste separation at the business level":1})
            df_q3 = pd.DataFrame(q3)
            df_temp = pd.concat([df_temp,df_q3])
            #print(df_q3)
            #q4 = df_q3.drop(['_id'],axis=1)
        q4=df_temp.drop(['_id'],axis=1)
            #print(q4)
        q5 = q4.rename(columns={"Extend of waste dispersed in the city":"Waste Dispersed"
                                ,"Hazardous waste being treated":"Waste Treated"
                                ,"Extend of plastic waste separation at the municipality level":"Plastic"
                                ,"Extend of paper waste separation at the municipality level":"Paper"
                                ,"Extend of metal waste separation at the municipality level":"Metal"
                                ,"Extend of glass waste separation at the municipality level":"Glass"
                                ,"Extend of organic waste separation at the municipality level":"Organic"
                                ,"Extend of battery separation at the municipality level":"Battery"
                                ,"Extend of medical waste separation at the healthcare centers":"Medical"
                                ,"Extend of electric and electronic waste separation at the municipality level":"Electronic"
                                ,"Extend of waste separation at the house level":"House Level Separation"
                                ,"Extend of waste separation at the business level":"Business Level"})
        #print(q5)
        q6 = q5.transpose()
        q7 = q6.drop(q6.index[0])
        q7.plot(kind='bar')
        plt.legend(['2008','2009'],loc= 'lower left',bbox_to_anchor=(0.0,1.0), ncol=2
                   , borderaxespad=0,frameon=False)
        plt.show()




