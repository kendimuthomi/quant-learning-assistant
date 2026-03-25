import streamlit as st
from logic import get_topic_data

st.set_page_config(page_title="Quant Learning Assistant", page_icon="📘")

st.title("📘 Quant Learning Assistant")
st.markdown("Learn basic quant and finance concepts in simple language.")

topic = st.text_input("Enter a quant or finance topic", placeholder="e.g. alpha, volatility, sharpe ratio")

if st.button("Explain Topic"):
    result = get_topic_data(topic)

    if result:
        st.subheader("Explanation")
        st.write(result["explanation"])

        st.subheader("Example")
        st.write(result["example"])

        st.subheader("Common Mistake")
        st.write(result["common_mistake"])

        st.subheader("Quiz Questions")
        for question in result["quiz"]:
            st.write(f"- {question}")
    else:
        st.warning("Topic not found. Try alpha, volatility, or sharpe ratio.")