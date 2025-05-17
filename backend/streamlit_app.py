import streamlit as st
from manager import calculate_processing, get_ingredients

potions_elements = ["health di tier 0", "health di tier 1", "health di tier 2", "anthidot di tier 1", "anthidot di tier 2", "mending di tier 0", "mending di tier 1", "mending di tier 2",
     "slowness", "swiftness di tier 1", "swiftness di tier 2", "slow_fall", "jump1", "jump di tier 2", "weakness",
     "revify", "damage", "shrink", "levitation", "grow", "poison", "invisibility",
     "dolphin ", "combustion", "strength", "impact", "holy", "fire", "frost", "arcane"]

# Sidebar curtain to choose between elements
element = st.selectbox(
    "Scegli la tua pozza preferita:", potions_elements
)

# Input cell for integer
input_value = st.number_input("Metti quante pozze vuoi:", min_value=1, step=1, format="%d")

# Checkbox for additional option
checkbox_value = st.checkbox("Maggiori dettagli")
            
# Button to send values
if st.button("Calcola"):
    result = calculate_processing(element, input_value, False)

    if isinstance(result, (list, tuple)) and len(result) >= 3:
        message = (
            f"No materiali: {round(result[0], 2) if isinstance(result[0], float) else result[0]} bronzini.\n"
            f"Solo materiali: {round(result[1], 2) if isinstance(result[1], float) else result[1]} bronzini.\n"
            f"Materiali e fuel: {round(result[2], 2) if isinstance(result[2], float) else result[2]} bronzini."
        )
        # Capitalize each line after splitting by \n
        message = "\n".join(line.capitalize() for line in message.split('\n'))
        st.markdown(message.replace('\n', '  \n'))
    else:
        st.error("Errore nel calcolo: risultato non valido.")

    if checkbox_value:
        # Map element name to potion_id (index in crafting)
        potion_names = potions_elements
        try:
            potion_id = potion_names.index(element)
        except ValueError:
            st.warning("Elemento non trovato.")
        df = get_ingredients(potion_id, input_value)
        st.markdown("### Dettaglio ingredienti")
        st.dataframe(df, hide_index=True)