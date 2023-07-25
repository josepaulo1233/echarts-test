from streamlit_echarts import st_echarts
import streamlit as st

tab1, tab2 = st.tabs(['Line', 'Bar'])

with tab1:
    options = {
    "xAxis": {
        "type": "category",
        "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "line"}
    ],
    }
    st_echarts(options=options)

with tab2:
    options = {
        "xAxis": {
            "type": "category",
            "data": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        },
        "yAxis": {"type": "value"},
        "series": [
            {"data": [820, 932, 901, 934, 1290, 1330, 1320], "type": "bar"}
        ],
    }
    st_echarts(options=options)