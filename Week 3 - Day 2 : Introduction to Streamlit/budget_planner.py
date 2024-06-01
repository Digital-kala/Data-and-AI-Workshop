import pandas as pd
import streamlit as st

# Set page configuration
st.set_page_config(page_title="Budget Planner", layout="wide", page_icon="📋")

# Initialize session state for budgets and transactions
if "budgets" not in st.session_state:
    st.session_state.budgets = []

if "transactions" not in st.session_state:
    st.session_state.transactions = []

if "toast" in st.session_state:
  st.toast(st.session_state.toast)
  del st.session_state.toast

# Function to add a new budget
def add_budget(category, amount):
    st.session_state.budgets.append({"Category": category, "Amount": amount})
    st.session_state.toast = f"💾 &nbsp; Added new budget for {category}"
    st.rerun()  # Rerun the app to refresh the state

# Function to add a new transaction
def add_transaction(category, description, amount):
    st.session_state.transactions.append({"Category": category, "Amount": amount, "Description": description})
    st.session_state.toast = f"💾 &nbsp; Added new transaction for {category}"
    st.rerun()  # Rerun the app to refresh the state

# Create columns for the layout
left, right = st.columns(2)

# Function to get the delta value for the metrics
def get_delta(value, symbol):
  return f"- {symbol}{abs(value):,.0f}" if value < 0 else f"{symbol}{value:,.0f}"

# Define a dialog for adding a new budget
@st.experimental_dialog("New Budget")
def add_new_budget():
    category = st.text_input("Budget Category")
    amount = st.number_input("Budget Amount", min_value=0)
    submitted = st.button("Add Budget")
    if submitted:
        add_budget(category, amount)

with left:
    # Left side: Budget board and form to add new budgets
    left.subheader("Budget Board", divider=True)
    
    # Display budgets as metrics
    if st.session_state.budgets:
        sub_col1, sub_col2 = st.columns(2)
        total_budget = sum(b['Amount'] for b in st.session_state.budgets)
        total_spent = sum(t['Amount'] for t in st.session_state.transactions)
        
        # Display total budget and total spent as metrics
        sub_col1.metric(label="💰 &nbsp; Total Budget", value=f"${total_budget:,.0f}")
        sub_col2.metric(label="🧾 &nbsp; Total Spent", value=f"${total_spent:,.0f}", delta=get_delta(total_budget - total_spent, "$"))
        st.divider()

        # Display each budget category as a metric
        rows = [st.session_state.budgets[i:i + 3] for i in range(0, len(st.session_state.budgets), 3)]
        for row in rows:
            cols = st.columns(3)
            for col, budget in zip(cols, row):
                total_amount = budget['Amount']
                total_spent = sum(t['Amount'] for t in st.session_state.transactions if t['Category'] == budget['Category'])
                difference = total_amount - total_spent
                col.metric(label=budget['Category'], value=f"${budget['Amount']:,.0f}", delta=get_delta(total_budget - total_spent, "$"))
    else:
        st.info("Add a new budget to get started", icon="ℹ️")
    
    st.markdown("<br/>", unsafe_allow_html=True)
    if st.button("➕ &nbsp; Add New Budget"):
        add_new_budget()

# Define a dialog for adding a new transaction
@st.experimental_dialog("New Transaction")
def add_new_transaction():
    transaction_category = st.selectbox("Budget Category", [b["Category"] for b in st.session_state.budgets])
    transaction_amount = st.number_input("Transaction Amount", min_value=0.0, format="%.0f")
    description = st.text_input("Transaction Description")
    transaction_submitted = st.button("Add Transaction")
    if transaction_submitted:
        add_transaction(transaction_category, description, transaction_amount)

# Right side: Form to add transactions and list of transactions
with right:
    st.subheader("Transactions", divider=True)
    
    # Display transactions in a dataframe if there are any
    if st.session_state.transactions:
        transaction_df = pd.DataFrame(st.session_state.transactions)
        
        # Create column config to display amount as currency
        column_config = {
            "Amount": st.column_config.NumberColumn(format="$ %d"),
        }
        
        # Display and allow editing of the transactions dataframe
        edited_df = st.data_editor(
            transaction_df, 
            use_container_width=True, 
            column_config=column_config,
            disabled=["Category", "Amount"]
        )
        
        # Update the dataframe with the edited data
        transaction_df = edited_df
    
    if not st.session_state.budgets:
        st.info("Add a new budget to get started", icon="ℹ️")
    else:
        st.markdown("<br/>", unsafe_allow_html=True)
        if st.button("➕ &nbsp; Add New Transaction"):
            add_new_transaction()
