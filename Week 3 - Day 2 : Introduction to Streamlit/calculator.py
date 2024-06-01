import streamlit as st

# Set the page title and icon for the Streamlit app
st.set_page_config(page_title="Calculator", page_icon="🧮")

def handle_button_click(btn):
    if btn == '=':
        try:
            # Evaluate the expression
            st.session_state.screen = str(eval(st.session_state.screen))
        except Exception as e:
            st.session_state.screen = "Error"
    elif btn == 'C':
        # Clear the screen
        st.session_state.screen = ""
    else:
        # Clear the screen if there was an error
        if st.session_state.screen == "Error":
            st.session_state.screen = ""
        
        if len(btn) > 1: 
          btn = btn[1]
        
        # Update the current screen
        st.session_state.screen += btn

# Initialize session state for storing current input and result
if "screen" not in st.session_state:
    st.session_state.screen = ""

# Create a display screen
st.text_input("Calculator",value=st.session_state.screen, disabled=True)

# Define button layout
buttons = [
    ['7', '8', '9', 'C'],
    ['4', '5', '6', '\*'],
    ['1', '2', '3', '\-'],
    ['0', '\+', '=', '/']
]

# Create buttons and handle button clicks
for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if cols[i].button(btn, use_container_width=True):
            handle_button_click(btn)
            st.rerun()
