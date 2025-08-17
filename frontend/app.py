import streamlit as st
from add_update import add_update_tab
from analytics_by_category import analytics_tab


st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["➕ Add/Update", "📊 Analytics By Category"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()

# changing the color of columns
import streamlit as st

# Inject CSS for column colors
st.markdown("""
    <style>
    /* First column */
    .col1 {
        background-color: #1E90FF;  /* blue */
        padding: 15px;
        border-radius: 10px;
        color: white;
    }
    
    /* Second column */
    .col2 {
        background-color: #FF6C37;  /* orange */
        padding: 15px;
        border-radius: 10px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)




# Inject CSS
tab_style = """
<style>
/* Tab container */
.stTabs [data-baseweb="tab-list"] {
    gap: 20px;
}

/* Inactive tabs */
.stTabs [data-baseweb="tab"] {
    color: white;
    background-color: #1f1f1f;   /* dark grey */
    border-radius: 10px 10px 0px 0px;
    padding: 10px 20px;
    font-weight: bold;
}

/* Active tab */
.stTabs [aria-selected="true"] {
    color: #fff !important;
    background-color: #FF6C37 !important;  /* orange highlight */
}
</style>
"""
st.markdown(tab_style, unsafe_allow_html=True)




# Custom CSS
page_bg = """
<style>
    .stApp {
        background-image: url("https://cdn.prod.website-files.com/607837a92aca1bb50efd05a0/667c73cbcea59c7e7a51b178_How%20to%20create%20a%20business%20expense%20report.png");
        background-size: cover;
    }
</style>
"""

st.markdown(page_bg, unsafe_allow_html=True)

