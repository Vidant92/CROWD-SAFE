import streamlit as st
import numpy as np

try:
    st.image(np.zeros((100, 100, 3)), width="stretch")
    print("Image stretch works")
except Exception as e:
    print(f"Image stretch error: {e}")

try:
    import plotly.express as px
    fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
    st.plotly_chart(fig, width="stretch")
    print("Plotly stretch works")
except Exception as e:
    print(f"Plotly stretch error: {e}")
