import pandas as pd
import os
import glob
import logging
from .crafting_ls import get_crafting

crafting = get_crafting()

# Initialize logger
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def read_csv_file():
    # Use the directory of this script as the base path
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    print(os.path.join(data_dir, '*.csv*'))
    for filepath in glob.glob(os.path.join(data_dir, '*.csv*')):
        print(f"filepath: {filepath}") 
        if not filepath:
            raise FileNotFoundError(f"No .csv file found in {data_dir}")
        return pd.read_csv(filepath)
    
def get_ingredients(potion_id, amount):
    df = read_csv_file()
    if df is None:
        logging.error("No CSV file found or failed to read CSV file.")
        return [0, 0, 0]
    
    header_row_index = 0
    ingredient_list = []
    
    df = df.iloc[header_row_index:]
    if potion_id < 0 or potion_id >= len(crafting):
        return pd.DataFrame(columns=["Ingrediente", "Quantità", "Prezzo unitario", "Prezzo totale"])
    ingredients = crafting[potion_id]
    for i in range(0, len(ingredients), 2):
        ingredient_name = str(ingredients[i])
        ingredient_amount = float(ingredients[i+1]) * amount
        price = None
        for _, row in df.iterrows():
            if str(row.get("ingredienti")) == ingredient_name:
                price = row.get("costo")
                break
        if pd.isna(price):
            price = 0
        total_price = ingredient_amount * float(price)

        # Round numbers: 2 decimals, but if within 0.1 of next integer, round up
        def smart_round(val):
            rounded = round(val, 2)
            if abs(rounded - round(rounded)) >= 0.9:
                return float(int(rounded) + 1)
            return rounded

        ingredient_list.append({
            "Ingrediente": ingredient_name,
            "Quantità": smart_round(ingredient_amount),
            "Prezzo unitario": smart_round(float(price)),
            "Prezzo totale": smart_round(total_price)
        })
    return pd.DataFrame(ingredient_list)
    
def get_cost(potion_id, amount, guadagno):
    df = read_csv_file()
    if df is None:
        logging.error("No CSV file found or failed to read CSV file.")
        return [0, 0, 0]
    
    header_row_index = 0
    df = df.iloc[header_row_index:]     # Get data of the header row
    
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
                        logging.info(f"Found ingredient: {str(ingredients[i])} in row: {src_ingredient} || with amount: {str(ingredients[i+1])} and cost: {float(costo_value)} => {cost_resoult}")
    cost_resoult[0] += guadagno
    cost_resoult[1] += guadagno
    cost_resoult[2] += guadagno
    logging.info(f"With guadagno: {guadagno}")
    return cost_resoult