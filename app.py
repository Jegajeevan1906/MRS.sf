import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 MRS Sales Dashboard")

# File uploader
uploaded_file = st.file_uploader("📂 Upload your CSV file", type=["csv"])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("✅ Original Data", data)

    # Sort data
    sorted_data = data.sort_values(by="Amt", ascending=False)
    st.write("📌 Sorted Data (Descending)", sorted_data)

    # Plot chart
    fig, ax = plt.subplots()
    ax.bar(sorted_data["Emp Name"], sorted_data["Amt"], color="skyblue")
    ax.set_title("Sales Amount by Employees (Descending)")
    ax.set_xlabel("Emp Name")
    ax.set_ylabel("Amt")
    st.pyplot(fig)
