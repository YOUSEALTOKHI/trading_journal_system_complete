"""Streamlit Web Interface"""
import streamlit as st
import pandas as pd
from datetime import datetime
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from config.config import Config
from database.models import Trade, get_session

st.set_page_config(
    page_title="Trading Journal",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Trading Journal System")

# Sidebar
with st.sidebar:
    page = st.radio("Navigation", [
        "Dashboard",
        "Add Trade",
        "Daily Analysis",
        "Van Tharp Principles"
    ])

if page == "Dashboard":
    st.header("Dashboard")
    st.write("Welcome to your Trading Journal!")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Trades", "0")
    with col2:
        st.metric("Win Rate", "0%")
    with col3:
        st.metric("Total P&L", "$0.00")

elif page == "Add Trade":
    st.header("Add New Trade")

    with st.form("add_trade"):
        col1, col2 = st.columns(2)

        with col1:
            symbol = st.selectbox("Symbol", ["EURUSD", "GBPUSD", "USDJPY"])
            trade_type = st.selectbox("Type", ["BUY", "SELL"])
            entry_price = st.number_input("Entry Price", min_value=0.0)

        with col2:
            exit_price = st.number_input("Exit Price", min_value=0.0)
            volume = st.number_input("Volume", min_value=0.01)
            profit_loss = st.number_input("Profit/Loss")

        if st.form_submit_button("Save Trade"):
            st.success("Trade saved!")

elif page == "Van Tharp Principles":
    st.header("Van Tharp's Ten Principles")

    for i, principle in enumerate(Config.VAN_THARP_PRINCIPLES, 1):
        st.write(f"{i}. {principle}")

st.markdown("---")
st.markdown("Trading Journal System v1.0.0")
