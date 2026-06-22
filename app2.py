import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="Fresher Hiring Analytics Dashboard",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

df = pd.read_csv("fresher_hiring_india_dataset.csv")
# --------------------------------------------------
# TITLE
# --------------------------------------------------

st.title("📊 Fresher Hiring Analytics Dashboard")
st.markdown("### Smart Hiring Trend Analysis")

# --------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------

st.sidebar.header("Filters")

degree_filter = st.sidebar.multiselect(
    "Select Degree",
    options=df["degree"].dropna().unique()
)

stage_filter = st.sidebar.multiselect(
    "Select Hiring Stage",
    options=df["hiring_stage"].dropna().unique()
)

if degree_filter:
    df = df[df["degree"].isin(degree_filter)]

if stage_filter:
    df = df[df["hiring_stage"].isin(stage_filter)]

# --------------------------------------------------
# KPI CARDS
# --------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Total Candidates",
    df.shape[0]
)

col2.metric(
    "Columns",
    df.shape[1]
)

col3.metric(
    "Missing Values",
    int(df.isnull().sum().sum())
)

col4.metric(
    "Avg CGPA",
    round(df["cgpa"].mean(), 2)
)

st.divider()

# --------------------------------------------------
# TABS
# --------------------------------------------------

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📄 Dataset",
    "📊 Visualizations",
    "📈 Statistics",
    "💼 Hiring Analysis",
    "🔍 Data Quality",
    "📌 Insights"
])

# --------------------------------------------------
# DATASET TAB
# --------------------------------------------------

with tab1:

    st.subheader("Dataset Preview")

    st.dataframe(df.head())

    st.subheader("Dataset Shape")

    st.write(df.shape)

    st.subheader("Data Types")

    st.dataframe(df.dtypes.astype(str))

# --------------------------------------------------
# VISUALIZATION TAB
# --------------------------------------------------

with tab2:

    st.subheader("Hiring Stage Distribution")

    stage = df["hiring_stage"].value_counts()

    fig = px.bar(
        x=stage.index,
        y=stage.values,
        labels={"x":"Hiring Stage","y":"Count"}
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Salary Distribution")

    fig2 = px.histogram(
        df,
        x="offered_salary_inr",
        nbins=30
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Degree Distribution")

    degree = df["degree"].value_counts()

    fig3 = px.bar(
        x=degree.index,
        y=degree.values
    )

    st.plotly_chart(fig3, use_container_width=True)

# --------------------------------------------------
# STATISTICS TAB
# --------------------------------------------------

with tab3:

    st.subheader("Summary Statistics")

    st.dataframe(df.describe())

    st.subheader("Correlation Matrix")

    numeric_df = df.select_dtypes(include=np.number)

    corr = numeric_df.corr()

    fig, ax = plt.subplots(figsize=(10,6))

    sns.heatmap(
        corr,
        annot=True,
        cmap="coolwarm",
        ax=ax
    )

    st.pyplot(fig)

# --------------------------------------------------
# HIRING ANALYSIS TAB
# --------------------------------------------------

with tab4:

    st.subheader("Average CGPA by Hiring Stage")

    cgpa = df.groupby(
        "hiring_stage"
    )["cgpa"].mean()

    st.bar_chart(cgpa)

    st.subheader("Certification Impact")

    cert = df.groupby(
        "hiring_stage"
    )["certifications_count"].mean()

    st.bar_chart(cert)

    st.subheader("Project Impact")

    proj = df.groupby(
        "hiring_stage"
    )["projects_count"].mean()

    st.bar_chart(proj)

# --------------------------------------------------
# DATA QUALITY TAB
# --------------------------------------------------

with tab5:

    st.subheader("Missing Values")

    missing = df.isnull().sum()

    st.dataframe(
        missing[missing > 0]
    )

    st.subheader("Duplicate Rows")

    duplicates = df.duplicated().sum()

    st.metric(
        "Duplicates",
        duplicates
    )

# --------------------------------------------------
# INSIGHTS TAB
# --------------------------------------------------

with tab6:

    st.subheader("Key Insights")

    st.markdown("""
    ✅ Higher CGPA improves hiring chances.

    ✅ Internship experience increases employability.

    ✅ Certifications positively influence recruitment.

    ✅ Practical projects enhance selection probability.

    ✅ Salary varies significantly across sectors.

    ✅ Technical and analytical skills remain highly demanded.

    ✅ Referrals contribute to better hiring outcomes.
    """)

    st.success(
        "Candidates with strong academics, projects, internships, and certifications tend to receive better hiring outcomes and salary offers."
    )