import streamlit as st
import requests



with st.sidebar:
    st.title("Тестовое")
    st.page_link("main.py", label="README", icon="🏠")
    st.subheader("Задание 1")
    st.page_link("pages/city_chat.py", label="Город из сообщения | чат", icon="1️⃣")
    st.page_link("pages/city_file.py", label="Город из сообщения | файл", icon="2️⃣")
    st.subheader("Задание 2")
    st.page_link("pages/random_greeting.py", label="Рандомное приветсвие", icon="1️⃣")

st.text_input("Имя:",value="Иван", key="input_message2")
st.button("Сгенерировать поздравление", key="submitted2")

if st.session_state["submitted2"]:

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
    headers = {
        "accept": "application/json",
        "Authorization": f"Api-Key {st.secrets['token']}",
        "Content-Type": "application/json"
    }

    body = {
    "modelUri": "gpt://b1gfl2975iijeg2iqtc0/yandexgpt-lite/latest",
    "completionOptions": {
        "stream": False,
        "temperature": 0.5,
        "maxTokens": 200
    },
    "messages": [
        {
        "role": "system",
        "text":  "Ты - чат-бот, генерирующий поздравления с днем рождения. В сообщении указано имя, напиши оригинальное поздравление, адресованное этому человеку."
        },
        {
        "role": "user",
        "text": st.session_state["input_message2"]
        }
    ]
    }
    response = requests.post(url, headers=headers, json=body).json()
    try:
        greeting = response.get("result","").get("alternatives","")[0].get("message","").get("text","")
        st.success(greeting)
    except:
        st.error("Квота закончилась")
    