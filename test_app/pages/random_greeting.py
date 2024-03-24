import streamlit as st

with st.sidebar:
    st.title("Тестовое")
    st.page_link("main.py", label="README", icon="🏠")
    st.subheader("Задание 1")
    st.page_link("pages\\city_chat.py", label="Город из сообщения | чат", icon="1️⃣")
    st.page_link("pages\\city_file.py", label="Город из сообщения | файл", icon="2️⃣")
    st.subheader("Задание 2")
    st.page_link("pages\\random_greeting.py", label="Рандомное приветсвие", icon="1️⃣")