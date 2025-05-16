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
            [   # antidoto
                'carbonella', 1,
                'core fragment', 1,
                'boccette', 1,
                'brim powder', 1,
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
    
