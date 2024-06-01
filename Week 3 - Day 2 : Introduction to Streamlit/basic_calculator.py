import streamlit as st

# Set the page title and icon for the Streamlit app
st.set_page_config(page_title="Simple Calculator", page_icon="🧮")

# Display the title of the app
st.subheader("Simple Calculator", divider=True)

# Create three columns for user inputs
col1, col2, col3 = st.columns(3)

# Input fields for the first and second numbers, and the operation type
number1 = col1.number_input("Enter the first number", value=0)
number2 = col2.number_input("Enter the second number", value=0)
operation = col3.selectbox("Choose the operation", ("Add", "Subtract", "Multiply", "Divide"))

# Button to perform the calculation
if st.button("Calculate"):
    # Perform the calculation based on the selected operation
    if operation == "Add":
        result = number1 + number2
    elif operation == "Subtract":
        result = number1 - number2
    elif operation == "Multiply":
        result = number1 * number2
    elif operation == "Divide":
        if number2 != 0:
            result = number1 / number2
        else:
            result = "Cannot divide by zero"

    # Display the result of the calculation
    st.write(f"The result is: {result}")