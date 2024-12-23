#!/usr/bin/env python

"""
As The Historians wander around a secure area at Easter Bunny HQ, you come across posters for a LAN party scheduled for today! Maybe you can find it; you connect to a nearby datalink port and download a map of the local network (your puzzle input).

The network map provides a list of every connection between two computers. For example:

kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn
Each line of text in the network map represents a single connection; the line kh-tc represents a connection between the computer named kh and the computer named tc. Connections aren't directional; tc-kh would mean exactly the same thing.

LAN parties typically involve multiplayer games, so maybe you can locate it by finding groups of connected computers. Start by looking for sets of three computers where each computer in the set is connected to the other two computers.

In this example, there are 12 such sets of three inter-connected computers:

aq,cg,yn
aq,vc,wq
co,de,ka
co,de,ta
co,ka,ta
de,ka,ta
kh,qp,ub
qp,td,wh
tb,vc,wq
tc,td,wh
td,wh,yn
ub,vc,wq
If the Chief Historian is here, and he's at the LAN party, it would be best to know that right away. You're pretty sure his computer's name starts with t, so consider only sets of three computers where at least one computer's name starts with t. That narrows the list down to 7 sets of three inter-connected computers:

co,de,ta
co,ka,ta
de,ka,ta
qp,td,wh
tb,vc,wq
tc,td,wh
td,wh,yn
Find all the sets of three inter-connected computers. How many contain at least one computer with a name that starts with t?
"""

with open('input','r') as f:
    data = f.read().splitlines()


edges = [l.split("-") for l in data]

connections = {}

for edge in edges:
    if edge[0][0] == 't':
        connections[edge[0]] =  connections.get(edge[0],[]) + [edge[1]]
    if edge[1][0] == 't':
        connections[edge[1]] =  connections.get(edge[1],[]) + [edge[0]]

cliques = []
for t_computer in connections:
    for i1 in range(len(connections[t_computer])):
        for i2 in range(i1 + 1,len(connections[t_computer])):
            c1 = connections[t_computer][i1]
            c2 = connections[t_computer][i2]
            if [c1, c2] in edges or [c2, c1] in edges:
                #ugly af lol
                cliques += [tuple(sorted([c1,c2, t_computer]))]
print(len(set(cliques)))

