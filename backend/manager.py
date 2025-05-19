from src.potion_operator import get_ingredients, get_cost

def calculate_processing(potion_id, amount, checkbox, guadagno):
    Potions = {
        "health di tier 0": 0,
        "health di tier 1": 1,
        "health di tier 2": 2,
        "anthidot": 3,
        "anthidot di tier 2": 4,
        "mending di tier 0": 5,
        "mending di tier 1": 6,
        "mending di tier 2": 7,
        "slowness": 8,
        "swiftness di tier 1": 9,
        "swiftness di tier 2": 10,
        "slow_fall": 11,
        "jump di tier 1": 12,
        "jump di tier 2": 13,
        "weakness": 14,
        "revify": 15,
        "damage": 16,
        "shrink": 17,
        "levitation": 18,
        "grow": 19,
        "poison": 20,
        "invisibility": 21,
        "dolphin ": 22,
        "combustion": 23,
        "strength": 24,
        "impact": 25,
        "holy": 26,
        "fire": 27,
        "frost": 28,
        "arcane": 29,
    }
    
    potion_selected = Potions.get(potion_id)
    if potion_selected is None:
        return "Potion not found"
    
    if checkbox:
        return get_ingredients(potion_selected, amount)
    else:
        return get_cost(potion_selected, amount, guadagno)
    
    