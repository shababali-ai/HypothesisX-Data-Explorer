import streamlit as st
import pandas as pd
from data_explorer import load_data, explore_data

st.set_page_config(
    page_title="HypothesisX AI - Data Explorer",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 HypothesisX AI — Data Explorer")
st.write(
    "Upload a CSV or Excel dataset and the Data Explorer will inspect its "
    "basic structure before the other AI agents investigate it."
)

st.sidebar.header("Dataset")
uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel file",
    type=["csv", "xlsx", "xls"]
)

# Optional sample dataset
sample_path = "data/simulated_weather.xlsx"

if uploaded_file is not None:
    try:
        df = load_data(uploaded_file)
    except Exception as e:
        st.error(f"Could not read the file: {e}")
        st.stop()
elif st.sidebar.button("Use Sample Weather Dataset"):
    df = pd.read_excel(sample_path)
else:
    st.info("👈 Upload a CSV/Excel file from the sidebar to begin.")
    st.stop()

report = explore_data(df)

st.success("Dataset loaded successfully!")

# Main overview
st.subheader("📊 Dataset Overview")
c1, c2, c3, c4 = st.columns(4)

c1.metric("Rows", report["rows"])
c2.metric("Columns", report["columns"])
c3.metric("Missing Cells", int(df.isnull().sum().sum()))
c4.metric("Duplicate Rows", report["duplicate_rows"])

# Preview
st.subheader("👀 Data Preview")
st.dataframe(df.head(10), use_container_width=True)

# Data types
st.subheader("🧩 Column Information")
column_info = pd.DataFrame({
    "Column": df.columns,
    "Data Type": [str(df[col].dtype) for col in df.columns],
    "Missing Values": [int(df[col].isnull().sum()) for col in df.columns],
    "Unique Values": [int(df[col].nunique(dropna=True)) for col in df.columns],
})
st.dataframe(column_info, use_container_width=True)

# Statistics
st.subheader("📈 Basic Statistics")
st.dataframe(df.describe(include="all").transpose(), use_container_width=True)

# Missing values
st.subheader("⚠️ Missing Values")
missing = df.isnull().sum().reset_index()
missing.columns = ["Column", "Missing Values"]
missing = missing[missing["Missing Values"] > 0]

if missing.empty:
    st.success("No missing values found.")
else:
    st.dataframe(missing, use_container_width=True)

# Duplicate rows
st.subheader("🔁 Duplicate Rows")
if report["duplicate_rows"] == 0:
    st.success("No duplicate rows found.")
else:
    st.warning(f"{report['duplicate_rows']} duplicate rows found.")

st.divider()
st.caption("HypothesisX AI • Data Explorer Agent")
