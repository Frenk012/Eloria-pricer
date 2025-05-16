import pandas as pd
import os
import glob
import logging

def get_ingredients(potion_id, amount):
    # Placeholder function to simulate getting ingredients
    # In a real application, this would query a database or perform calculations
    return f"Ingredients for potion {potion_id} with amount {amount}"

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_cost(potion_id, amount):
    data_dir = os.path.join(os.getcwd(), "data")
    print(os.path.join(data_dir, '*.csv*'))
    for filepath in glob.glob(os.path.join(data_dir, '*.csv*')):
        print(f"filepath: {filepath}") 
        if not filepath:
            raise FileNotFoundError(f"No .xlsx file found in {filepath}")
        df = pd.read_csv(filepath)

        header_row_index = next((i for i, row in df.iterrows() if "ingredienti" in row.values), None)
        
        df = df.iloc[header_row_index:]     # Get data of the header row
        
        crafting = [
            [   # cura t0
                'carbonella', 0.5,
                'boccette', 1,
                'heal cata 0', 0.5,
            ],
            [   # cura t1
                'carbonella', 0.3333,
                'boccette', 1,
                'heal cata 1', 0.3333,
            ],
            [   # cura t2
                'carbonella', 2,
                'boccette', 1,
                'heal cata 2', 1,
            ],
            [   # antidoto
                'carbonella', 1,
                'boccette', 1,
                'brim powder', 1,
                'carne marcia', 1,
            ],
            [   # antidoto t2
                'carbonella', 1,
                'revival star', 0.5,
                'boccette', 0.5,
                'organic resin', 0.5,
            ],
            [   # Mending T0
                'carbonella', 1,
                'core fragment', 1,
                'boccette', 1,
                'brim powder', 1,
            ],
            [   # Mending T1
                'carbonella', 1,
                'core fragment', 1,
                'boccette', 1,
                'organic resin', 1,
                'spider eye', 1,
            ],
            [   # Mending T2
                'carbonella', 2,
                'core fragment', 1,
                'boccette', 1,
                'organic resin', 1,
                'membrane', 1,
            ],
            [   # slowness
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # swiftness t1
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # swiftness t2
                'carbonella', 1,
                'core fragment', 1,
                'blaze powder', 1,
                'item random', 1,
            ],
            [   # slow fall
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # jump T1
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # jump t2
                'carbonella', 1,
                'core fragment', 1,
                'blaze powder', 1,
                'item random', 1,
            ],
            [   # weakness
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # revify
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'revival star', 1,
            ],
            [   # danno
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'spider eye', 1,
            ],
            [   # shrink
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'fungo marrone', 1,
            ],
            [   # levitation
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'ametista', 1,
            ],
            [   # grow
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'fungo rosso', 1,
            ],
            [   # poison
                'carbonella', 1,
                'boccette', 1,
                'core fragment', 1,
                'spider eye', 1,
                'fungo marrone', 1,
                'zucchero', 1,
            ],
            [   # invisibility
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
                'antracite', 1,
                'item random', 1,
            ],
            [   # dolphin 
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # combustion
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # strength
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # impact
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # holy
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # fire
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # frost
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ],
            [   # arcane
                'carbonella', 2,
                'boccette', 1,
                'core fragment', 1,
            ]
        ]
        cost_resoult = [0,0,0]
        for index in range(len(crafting)):
            if index == potion_id:
                ingredients = crafting[potion_id]
                for i in range(0, len(ingredients), 2):
                    logging.debug(f"i: {i}")
                    for index, row in df.iterrows():
                        src_ingredient = str(row.get("ingredienti"))
                        if str(ingredients[i]) == src_ingredient:
                            costo_value = row.get("costo")
                            if pd.isna(costo_value):
                                logging.warning(f"'costo' is NaN or missing for ingredient {src_ingredient}, skipping.")
                                continue
                            # Calculate cost
                            cost_resoult[0] += ((float(ingredients[i+1]) * amount) * (float(costo_value)))
                            if src_ingredient == "boccette" or src_ingredient == "giare" or src_ingredient == "carbonella":
                                cost_resoult[1] += ((float(ingredients[i+1]) * amount) * (float(costo_value)))
                            if src_ingredient == "boccette" or src_ingredient == "giare":
                                cost_resoult[2] += ((float(ingredients[i+1]) * amount) * (float(costo_value)))
                            logging.info(f"Found ingredient: {str(ingredients[i])} in row: {src_ingredient} with amount: {str(ingredients[i+1])} and cost: {float(costo_value)} => {cost_resoult}")
        return cost_resoult
    
