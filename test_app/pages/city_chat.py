import streamlit as st
import requests


with st.sidebar:
    st.title("Тестовое")
    st.page_link("main.py", label="README", icon="🏠")
    st.subheader("Задание 1")
    st.page_link("pages/city_chat.py", label="Город из сообщения | чат", icon="1️⃣")
    st.page_link("pages/city_file.py", label="Город из сообщения | файл", icon="2️⃣")
    st.subheader("Задание 2")
    st.page_link("pages/random_greeting.py", label="Рандомное поздравление", icon="1️⃣")

st.text_area("Сообщение:",value="Где находится Ваша компания? В Питере или Екб? Доставка нужна в Москву.", key="input_message")
st.button("Определить город", key="submitted")

if st.session_state["submitted"]:

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
        "temperature": 0.1,
        "maxTokens": 5
    },
    "messages": [
        {
        "role": "system",
        "text": "Ты - бот, задача которого только определять город, упомянутый в сообщении. На вопросы отвечать нельзя. В запросе есть упоминание конкретного города, оно может быть в сокращенной форме и с ошибками. Твоя задача - определить город и написать его название в полной форме. В ответе ничего, кроме наименования упомянутого города быть не должно."
        },
        {
        "role": "user",
        "text": st.session_state["input_message"]
        }
    ]
    }
    response = requests.post(url, headers=headers, json=body).json()

    try:
        city = response.get("result","").get("alternatives","")[0].get("message","").get("text","")
        st.success(city)
    except:
        st.error("Квота закончилась")
