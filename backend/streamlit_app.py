import streamlit as st
from manager import calculate_processing, get_ingredients

# nativefier --name "ElysiumPricer" "https://eloria-pricer.streamlit.app/" --platform windows --arch x64

potions_elements = ["health di tier 0", "health di tier 1", "health di tier 2", "anthidot di tier 1", "anthidot di tier 2", "mending di tier 0", "mending di tier 1", "mending di tier 2",
     "slowness", "swiftness di tier 1", "swiftness di tier 2", "slow_fall", "jump1", "jump di tier 2", "weakness",
     "revify", "damage", "shrink", "levitation", "grow", "poison", "invisibility",
     "dolphin ", "combustion", "strength", "impact", "holy", "fire", "frost", "arcane"]

# Sidebar to choose between "Alchimisti" and "Fattori"
# Add "Impostazioni" button at the top of the sidebar
if 'show_settings' not in st.session_state:
    st.session_state['show_settings'] = False

# Initialize guadagno in session_state if not present
if 'guadagno' not in st.session_state:
    st.session_state['guadagno'] = 0.0

# Inizializzazione dello stato
if 'show_settings' not in st.session_state:
    st.session_state['show_settings'] = False
if 'guadagno' not in st.session_state:
    st.session_state['guadagno'] = 0.0

# Placeholder per il bottone
button_placeholder = st.sidebar.empty()

# Etichetta dinamica
settings_label = "Impostazioni" if not st.session_state['show_settings'] else "Torna indietro"

# Cattura del click sul bottone
if button_placeholder.button(settings_label, key="settings_btn"):
    st.session_state['show_settings'] = not st.session_state['show_settings']
    # Forza il rerun per aggiornare subito l'etichetta del bottone
    st.rerun()

# Mostra le impostazioni se attive
if st.session_state['show_settings']:
    st.title("Impostazioni")
    st.session_state['guadagno'] = st.number_input(
        "Inserisci quanti bronzini vuoi guadagnare per pozione venduta:",
        min_value=0.0, format="%.2f", step=1.0, value=st.session_state['guadagno']
    )
    st.stop()

# Add some vertical space before the rest
st.sidebar.markdown("---")
st.sidebar.title("Seleziona una maestranza")
categoria = st.sidebar.radio("v", ("Alchimisti", "Fabbri", "Carpenteri"), label_visibility="collapsed")

# Add subcategories for Alchimisti
if categoria == "Alchimisti":
    sotto_categoria = st.sidebar.radio("Sezione alchimista:", ("Pozioni", "Crafting"))
    if sotto_categoria == "Pozioni":
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
            result = calculate_processing(element, input_value, False, st.session_state['guadagno'])

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
else:
    sotto_categoria = None

if categoria == "Fabbri":
    element = st.selectbox(
        "Boh:", ["boh"]
    )

if categoria == "Carpenteri":
    element = st.selectbox(
        "Boh:", ["boh"]
    )
