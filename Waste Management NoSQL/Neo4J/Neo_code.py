import pandas as pd
from neo4j import GraphDatabase
import networkx as nx
from py2neo import Graph, Node, Relationship

#uri = "bolt://localhost:11006"
neo = Graph(host='localhost', port=11006, password="test")


neo.run(''' match(n) detach delete n''')

q1 = '''load csv with headers from 'file:///nodes.csv' as house
create (n:house{ name:house.number, street:house.Street, Longitude:toFloat(house.Longitude) 
,Latitude:toFloat(house.Latitude), bin:house.bin_status})'''

neo.run(q1)

q2 = '''load csv with headers from 'file:///street.csv' as street
create (s:street{name:street.name, bin:street.bin, Latitude:toFloat(street.latitude), 
Longitude:toFloat(street.longitude)})'''

neo.run(q2)

q3 = '''load csv with headers from 'file:///nodes.csv' as house
match (a:house{name:house.number}),(b:street{name:house.Street})
create (a)-[r:LOCATED_ON]->(b)'''

neo.run(q3)

q4 = '''load csv with headers from 'file:///street_connect.csv' as street
match (c:street{name:street.name}),(d:street{name:street.connect})
create (c)-[r:CONNECTS_TO{cost:street.distance}]->(d)'''

neo.run(q4)

#q5 = '''match(n) return n'''

# assigned match and return query to variable 'a' so that it can be queried in the for loop
#a = neo_session.run(q5)
#for i in a:
#   print(i)

source = input('enter the source:')
dest = input('enter the destination:')

q6 = '''match(start:house{name:$param1}),(end:house{name:$param2})
call algo.shortestPath.astar.stream(start,end,'time','Latitude','Longitude')
yield nodeId,cost
return algo.asNode(nodeId).name as house, cost'''


b = neo.run(q6, parameters = {'param1': source, 'param2': dest})
for x in b:
	print(x)

source1 = input('enter the street name:')

q7 = '''Match p=(s:street {name: $param3})-[r:CONNECTS_TO*]-(Street:street) WHERE s.name <> Street.name and Street.bin = "Yes" and s.bin = "Yes"
WITH Street,[s in nodes(p)|s.name] as list ,REDUCE (sm = 0, k in r|  sm+k.distance) as sm ORDER BY sm
RETURN  Street.name as endNode, COLLECT(list)[0] as path,COLLECT(sm)[0] as weight'''

c = neo.run(q7, parameters = {'param3': source1 })
for y in c:
	print(y)


