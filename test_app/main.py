import streamlit as st

with st.sidebar:
    st.title("Тестовое")
    st.page_link("main.py", label="README", icon="🏠")
    st.subheader("Задание 1")
    st.page_link("pages\\city_chat.py", label="Город из сообщения | чат", icon="1️⃣")
    st.page_link("pages\\city_file.py", label="Город из сообщения | файл", icon="2️⃣")
    st.subheader("Задание 2")
    st.page_link("pages\\random_greeting.py", label="Рандомное приветсвие", icon="1️⃣")

st.title("Добрый день,")
st.write("Решения можно найти в боковом меню или по ссылкам:")
st.subheader("Задание 1")
st.page_link("pages\\city_chat.py", label="Город из сообщения | чат", icon="1️⃣")
st.page_link("pages\\city_file.py", label="Город из сообщения | файл", icon="2️⃣")
st.subheader("Задание 2")
st.page_link("pages\\random_greeting.py", label="Рандомное приветсвие", icon="1️⃣")
st.subheader("Дополнение")
st.write("Решение первого задания можно улучшить, добавив базу с известными сокращениями и использовав RAG (Retrieval Augmented Generation).")


from groq import Groq

client = Groq(
    api_key=st.secrets["groq_token"]
)
st.write(st.secrets["groq_token"])
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of low latency LLMs",
        }
    ],
    model="mixtral-8x7b-32768",
    temperature=0.5,
    max_tokens=5640,
    top_p=1,
    stream=True,
    stop=None,
)

st.write(chat_completion.choices[0].message.content)