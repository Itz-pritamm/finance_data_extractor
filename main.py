import streamlit as st
import pandas as pd
from data_extractor import extract

st.set_page_config(page_title="Financial Data Extractor")

# 1. Title
st.title("Financial Data Extractor")

# 2. Input box
article = st.text_area("Enter news article text", height=200)



# 3. Button
if st.button("Extract"):
    result = extract(article)

    # 4. Table
    df = pd.DataFrame({
        "Measure": ["Revenue", "EPS"],
        "Estimated": [
            result["revenue_expected"],
            result["eps_expected"]
        ],
        "Actual": [
            result["revenue_actual"],
            result["eps_actual"]
        ]
    })

    st.table(df)
