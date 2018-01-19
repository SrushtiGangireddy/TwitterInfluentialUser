import networkx as nx
import json
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

G = nx.DiGraph()

fileName = '886641057223585792.TRT.txt'
#counter=1
relationships = {}
with open(fileName,'r') as f:
        for line in f:
                if line != "":
                        json_acceptable_string = line.replace("'", "\"")
                        trt = json.loads(json_acceptable_string)
                        relationships = trt
#print(len(relationships.keys()))
G.add_nodes_from(relationships.keys())

for key,val in relationships.items():
        if len(val) > 0:
                for value in val:
                        G.add_edge(key,value)



#print(G.nodes())
#print(G.edges())

nx.draw(G)
plt.savefig("886641057223585792_Di_Path.png")
plt.show()

