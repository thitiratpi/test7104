# -*- coding: utf-8 -*-
"""test7104.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ccxltE5P_8CVEpOQ3tlnhFWktWFSayLF
"""

import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

# Mock database of food items
food_data = pd.DataFrame({
    "Food Item": ["Milk", "Eggs", "Cheese", "Yogurt", "Chicken", "Spinach"],
    "Category": ["Dairy", "Dairy", "Dairy", "Dairy", "Meat", "Vegetables"],
    "Expiry Date": [
        datetime.today() + timedelta(days=3),
        datetime.today() + timedelta(days=7),
        datetime.today() + timedelta(days=10),
        datetime.today() + timedelta(days=2),
        datetime.today() + timedelta(days=5),
        datetime.today() + timedelta(days=1)
    ]
})

# Convert expiry date to string for display
food_data["Expiry Date"] = food_data["Expiry Date"].dt.strftime("%Y-%m-%d")

# Navigation menu
st.sidebar.title("Food Expiry Alert System")
page = st.sidebar.radio("Go to", ["Login", "Food Categories", "Expiry Alerts"])

# Login Page
if page == "Login":
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if username == "admin" and password == "password":
            st.success("Login successful!")
            st.session_state["logged_in"] = True
        else:
            st.error("Invalid username or password")

# Food Categories Page
elif page == "Food Categories":
    st.title("Food Categories")
    categories = food_data["Category"].unique()
    selected_category = st.selectbox("Select a category", categories)
    filtered_food = food_data[food_data["Category"] == selected_category]
    st.write(filtered_food)

# Expiry Alerts Page
elif page == "Expiry Alerts":
    st.title("Food Expiry Alerts")
    today = datetime.today().strftime("%Y-%m-%d")
    expiring_soon = food_data[pd.to_datetime(food_data["Expiry Date"]) <= pd.to_datetime(today) + timedelta(days=3)]
    if not expiring_soon.empty:
        st.warning("The following food items are about to expire:")
        st.write(expiring_soon)
    else:
        st.success("No items are close to expiring!")