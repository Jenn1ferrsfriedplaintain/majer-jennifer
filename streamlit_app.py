import streamlit as st
import pandas as pd
import numpy as np

@st.cache_data
def load_data():
    return pd.read_csv("/kaggle/input/social-media-addiction-vs-relationships/Students Social Media Addiction.csv")


st.title("Students'Addiction Data")
st.write(
    "Description: This data set displays the addiction rates and details of students throughout the United States"
)

