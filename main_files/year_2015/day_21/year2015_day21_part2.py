# --- Part Two ---
# Turns out the shopkeeper is working with the boss, and can persuade you to buy whatever items he wants.
# The other rules still apply, and he still only has one of each item.
#
# What is the most amount of gold you can spend and still lose the fight?


from itertools import combinations, count

# constants
WEAPONS = {
    'Dagger': {
        'cost': 8, 'damage': 4, 'armor': 0
    },
    'Shortsword': {
        'cost': 10, 'damage': 5, 'armor': 0
    },
    'Warhammer': {
        'cost': 25, 'damage': 6, 'armor': 0
    },
    'Longsword': {
        'cost': 40, 'damage': 7, 'armor': 0
    },
    'Greataxe': {
        'cost': 74, 'damage': 8, 'armor': 0
    }
}

# all armor with additional 'None' Armor for convenience
ARMOR = {
    'Leather': {
        'cost': 13, 'damage': 0, 'armor': 1
    },
    'Chainmail': {
        'cost': 31, 'damage': 0, 'armor': 2
    },
    'Splintmail': {
        'cost': 53, 'damage': 0, 'armor': 3
    },
    'Bandedmail': {
        'cost': 75, 'damage': 0, 'armor': 4
    },
    'Platemail': {
        'cost': 102, 'damage': 0, 'armor': 5
    },
    'Bare': {
        'cost': 0, 'damage': 0, 'armor': 0
    }
}

RINGS = {
    'Damage +1': {
        'cost': 25, 'damage': 1, 'armor': 0
    },
    'Damage +2': {
        'cost': 50, 'damage': 2, 'armor': 0
    },
    'Damage +3': {
        'cost': 100, 'damage': 3, 'armor': 0
    },
    'Defense +1': {
        'cost': 20, 'damage': 0, 'armor': 1
    },
    'Defense +2': {
        'cost': 40, 'damage': 0, 'armor': 2
    },
    'Defense +3': {
        'cost': 80, 'damage': 0, 'armor': 3
    }
}

# boss input here
BOSS = {
    'damage': 8,
    'armor': 2,
    'hp': 100,
}


def game_handler() -> int:
    # Play all possible games with 1 weapon, 0 or 1 armor, <0-2> rings. Pick most expensive losing set.
    most_expensive = 0
    for weapon in WEAPONS.keys():
        for armor in ARMOR.keys():
            # rings (min 0, max 2)
            for i in range(0, 3):
                for rings_set in combinations(RINGS.keys(), i):
                    # calculate current hero stats
                    current_attack = WEAPONS[weapon]['damage'] + sum(RINGS[ring]['damage'] for ring in rings_set)
                    current_armor = ARMOR[armor]['armor'] + sum(RINGS[ring]['armor'] for ring in rings_set)
                    current_cost = WEAPONS[weapon]['cost'] + ARMOR[armor]['cost'] + sum(RINGS[ring]['cost'] for ring
                                                                                        in rings_set)
                    # simulate fight - if boss won, check current items set total price
                    if not simulate_fight_boss(current_attack, current_armor, 100):
                        most_expensive = max(most_expensive, current_cost)

    return most_expensive


def simulate_fight_boss(attack: int, armor: int, hp: int) -> bool:
    # initial fight information
    player_stats = {
        'damage': attack,
        'armor': armor,
        'hp': hp,
    }
    boss_stats = BOSS.copy()

    # simulate fight
    for game_round in count(0):
        # even - players turn, odd - boss turn (min 1 dmg)
        if game_round % 2 == 0:
            boss_stats['hp'] -= (player_stats['damage'] - boss_stats['armor']) or 1
        else:
            player_stats['hp'] -= (boss_stats['damage'] - player_stats['armor']) or 1

        # check if someone lost
        if boss_stats['hp'] <= 0:  # fight won, return True
            return True
        if player_stats['hp'] <= 0:  # fight lost, return False
            return False


if __name__ == '__main__':
    result = game_handler()
    print(f"Highest cost to lost the fight with boss: {result}")
