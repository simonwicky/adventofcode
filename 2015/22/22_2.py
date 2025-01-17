#!/usr/bin/env python
"""
On the next run through the game, you increase the difficulty to hard.

At the start of each player turn (before any other effects apply), you lose 1 hit point. If this brings you to or below 0 hit points, you lose.

With the same starting stats for you and the boss, what is the least amount of mana you can spend and still win the fight?
"""

#!/usr/bin/env python
"""
Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)

"""
#Did not want to code all this boilerplate, so credit to https://github.com/tomp/AOC-2015/blob/master/day22/day22.py

import heapq


class Spell(object):
    """
    A Spell represents the basic characteristics of a spell that
    can be cast by a wizard.

    cost ...... the cost in gold to the wizard to use the spell.
    damage .... the immediate damage done to the target when cast.
    turns ..... the number of turns that the spells effects apply.
                (This is zero if the spells only effects are immediate.)
    """
    def __init__(self, name, cost, turns=0):
        self.name = name
        self.cost = cost
        self.turns = turns

    def __gt__(self, spell2):
        return self.cost > spell2.cost

MISSILE_SPELL = Spell("Magic Missile", 53)
MISSILE_DAMAGE = 4

DRAIN_SPELL = Spell("Drain", 73)
DRAIN_HEALING = 2
DRAIN_DAMAGE = 2

POISON_SPELL = Spell("Poison", 173, turns=6)
POISON_DAMAGE = 3

RECHARGE_SPELL = Spell("Recharge", 229, turns=5)
RECHARGE_AMOUNT = 101

SHIELD_SPELL = Spell("Shield", 113, turns=6)
SHIELD_ENHANCEMENT = 7

# Available spells, in order of increasing cost
all_spells = (MISSILE_SPELL, DRAIN_SPELL, SHIELD_SPELL, POISON_SPELL, RECHARGE_SPELL)

class Player(object):
    def __init__(self, name, hitpoints, damage=0, armor=0, gold=0, mana=0,
            inventory=None):
        # Set intrinisic attributes of player
        self.name = name
        self._hitpoints = hitpoints
        self._damage = damage
        self._armor = armor
        # Set variable attributes
        self.reset()
        self.gold = gold
        self.mana = mana
        if inventory is not None:
            for item in inventory:
                self.pick_up(item)

    def reset(self):
        self.health = self._hitpoints
        self.armor = self._armor
        self.damage = self._damage
        self.gold = 0
        self.mana = 0
        self.inventory = []
        self.under_poison = 0
        self.under_recharge = 0
        self.under_shield = 0

    def pick_up(self, item):
        """
        Add the given item to the player's inventory.
        Update the player's armor and damage to reflect the new item.
        """
        self.inventory.append(item)
        self.armor += item.armor
        self.damage += item.damage

    def inventory_value(self):
        return sum([item.cost for item in self.inventory])

    def effective_armor(self):
        if self.under_shield:
            return self.armor + SHIELD_ENHANCEMENT
        else:
            return self.armor

    # On each turn, a player is expected to either attack or to cast a spell.
    # Start-of-turn logic is therefor built into these methods.
    def attack(self, opponent):
        if self.is_alive():
            opponent._attacked(self)

    def cast_spell(self, spell, opponent=None):
        assert spell.cost <= self.mana
        if self.is_alive():
            self.mana -= spell.cost
            if spell in (MISSILE_SPELL, DRAIN_SPELL, POISON_SPELL):
                assert opponent is not None
                opponent._spell_cast(spell)
                if spell == DRAIN_SPELL:
                    self.health += DRAIN_HEALING
            if spell in (SHIELD_SPELL, RECHARGE_SPELL):
                self._spell_cast(spell)
            

    def _attacked(self, opponent):
        """
        Player is attacked by given opponent.
        Returns True if player survives the attack, False if he's killed.
        """
        if self.health < 1:
            return False
        power = opponent.damage - self.effective_armor()
        if power < 1:
            power = 1
        self._damage_received(power)
        return self.is_alive()

    def _damage_received(self, damage, cause="blow"):
        if self.health >= damage:
            self.health -= damage
        else:
            self.health = 0
        return self.is_alive()

    def _spell_cast(self, spell):
        if self.health < 1:
            return False
        if spell == MISSILE_SPELL:
            return self._damage_received(MISSILE_DAMAGE, spell.name)
        elif spell == DRAIN_SPELL:
            return self._damage_received(DRAIN_DAMAGE, spell.name)
        elif spell == SHIELD_SPELL:
            if not self.under_shield:
                self.under_shield = spell.turns
        elif spell == POISON_SPELL:
            if not self.under_poison:
                self.under_poison = spell.turns
        elif spell == RECHARGE_SPELL:
            if not self.under_recharge:
                self.under_recharge = spell.turns

    def apply_spell_effects(self):
        if self.under_poison:
            self._damage_received(POISON_DAMAGE, POISON_SPELL.name)
            self.under_poison -= 1
        if self.under_recharge:
            self.mana += RECHARGE_AMOUNT
            self.under_recharge -= 1
        if self.under_shield:
            self.under_shield -= 1

    def would_defeat(self, opponent):
        """
        Evaluate who would win a fight to the death between the player
        and the given opponent, with the player striking first. (No magic.)
        Return True if the player would win, false if the opponent would win.
        """
        if opponent.damage > self.armor:
            damage_received = opponent.damage - self.armor
        else:
            damage_received = 1

        if self.damage > opponent.armor:
            damage_given = self.damage - opponent.armor
        else:
            damage_given = 1

        blows_received = (self.health + damage_received - 1) // damage_received
        blows_given = (opponent.health + damage_given - 1) // damage_given
        # log.debug("[blows given: {}, blows received: {}]".format(blows_given, blows_received))
        return blows_given <= blows_received

    def is_alive(self):
        return self.health > 0

def run_scenario(player, boss, spell_queue=[], deathmatch=True, hardmode=False):
    """
    Run battle between player and opponent destructively.
    (Input arguments are modified by play.)
    """
    while True:
        boss.apply_spell_effects()
        if not boss.is_alive():
            break

        player.apply_spell_effects()
        if hardmode:
            player._damage_received(1, "hard mode")
        if not player.is_alive():
            break

        if spell_queue:
            player.cast_spell(spell_queue.pop(0), boss)
        elif not deathmatch:
            return

        player.apply_spell_effects()
        boss.apply_spell_effects()
        if not boss.is_alive():
            break

        boss.attack(player)
        if not player.is_alive():
            break

def legal_spell(spell, seq):
    if spell.turns < 3:
        return True
    window = (spell.turns - 1) // 2
    if len(seq) > window:
        return spell not in seq[-window:]
    else:
        return spell not in seq

def cheapest_winning_spell_sequence(player_hitpoints=0, player_mana=0,
        boss_hitpoints=0, boss_damage=0, spells=None, hardmode=False):
    """
    Report the least expensive sequence of spells that defeat the boss, for the
    given player and boss attributes.

    A tuple of (cost, spell list) is returned.
    """
    assert spells is not None and len(spells) > 0

    fringe = []
    for s in spells:
        if s.cost <= player_mana:
            heapq.heappush(fringe, (s.cost, [s], player_mana - s.cost))

    while True:
        cost, seq, mana = heapq.heappop(fringe)
        you = Player("Player", hitpoints=player_hitpoints, mana=player_mana)
        boss = Player("Boss", hitpoints=boss_hitpoints, damage=boss_damage)
        run_scenario(you, boss, list(seq), deathmatch=False, hardmode=hardmode)
        if not boss.is_alive():
            return (cost, seq)

        if you.is_alive() and ((you.health // 3) + 1 >= (boss.health // 6)):
            for s in spells:
                if s.cost <= you.mana and legal_spell(s, seq):
                    heapq.heappush(fringe, (cost + s.cost, seq + [s], you.mana - s.cost))


with open('input', 'r') as f:
    data = f.read().splitlines()

boss_hitpoints = int(data[0].split(" ")[2])
boss_damage = int(data[1].split(" ")[1])

player_hitpoints = 50
player_mana = 500

cost, seq = cheapest_winning_spell_sequence(player_hitpoints, player_mana,
        boss_hitpoints, boss_damage, spells=all_spells, hardmode=True)
# print("Cost: {:4d}  Spells: {}".format(cost, ", ".join( [s.name
#     for s in seq])))
print(cost)
