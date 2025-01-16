#!/usr/bin/env python
"""
Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants. The other rules still apply, and he still only has one of each item.

What is the most amount of gold you can spend and still lose the fight?
"""

def fight(boss_hp, boss_dmg, boss_armor, player_hp, player_dmg, player_armor):
    boss_hp_loss_per_turn = max(1, player_dmg - boss_armor)
    player_hp_loss_per_turn = max(1, boss_dmg - player_armor)
    boss_dead_after_turn = boss_hp // boss_hp_loss_per_turn
    if boss_hp % boss_hp_loss_per_turn > 0:
        boss_dead_after_turn += 1

    player_dead_after_turn = player_hp // player_hp_loss_per_turn
    if player_hp % player_hp_loss_per_turn > 0:
        player_dead_after_turn += 1
    return player_dead_after_turn >= boss_dead_after_turn

with open('input','r') as f:
    data = f.read().splitlines()

boss_hp = int(data[0].split(" ")[2])
boss_dmg = int(data[1].split(" ")[1])
boss_armor = int(data[2].split(" ")[1])

player_hp = 100


weapons = [(8, 4), (10, 5), (25, 6), (40, 7), (74, 8)]
armors = [(0, 0), (13, 1), (31, 2), (53, 3), (75, 4), (102, 5)]
rings = [(0, 0, 0),(0, 0, 0),( 25,1,0),( 50,2,0),(100,3,0),( 20,0,1),( 40,0,2), ( 80,0,3)]


max_gold = 0
for w in weapons:
    for a in armors:
        for i in range(len(rings)):
            for j in range(i+1,len(rings)):
                gold = w[0] + a[0] + rings[i][0] + rings[j][0]
                if gold > max_gold:
                    player_dmg = w[1] + rings[i][1] + rings[j][1]
                    player_armor = a[1] + rings[i][2] + rings[j][2]
                    if not fight(boss_hp, boss_dmg, boss_armor, player_hp, player_dmg, player_armor):
                        print(w,a,rings[i], rings[j])
                        max_gold = gold


print(max_gold)