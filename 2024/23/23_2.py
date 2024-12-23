#!/usr/bin/env python
"""
There are still way too many results to go through them all. You'll have to find the LAN party another way and go there yourself.

Since it doesn't seem like any employees are around, you figure they must all be at the LAN party. If that's true, the LAN party will be the largest set of computers that are all connected to each other. That is, for each computer at the LAN party, that computer will have a connection to every other computer at the LAN party.

In the above example, the largest set of computers that are all connected to each other is made up of co, de, ka, and ta. Each computer in this set has a connection to every other computer in the set:

ka-co
ta-co
de-co
ta-ka
de-ta
ka-de
The LAN party posters say that the password to get into the LAN party is the name of every computer at the LAN party, sorted alphabetically, then joined together with commas. (The people running the LAN party are clearly a bunch of nerds.) In this example, the password would be co,de,ka,ta.

What is the password to get into the LAN party?
"""
#pip install networkx
try:
    import networkx as nx
except:
    print("Intall networkx first")
    exit(1)

with open('input','r') as f:
    data = f.read().splitlines()

G = nx.Graph()
for l in data:
    G.add_edge(*l.split("-"))


max_size = 0
clique = 0
for c in nx.find_cliques(G):
    if len(c) > max_size:
        max_size = len(c)
        clique = c
print(",".join(sorted(clique)))