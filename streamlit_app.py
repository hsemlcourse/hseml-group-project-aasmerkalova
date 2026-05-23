# streamlit_app.py
import streamlit as st
import requests
import json

st.set_page_config(page_title="Starbucks Revenue Predictor", layout="centered")
st.title("Предсказание суммы заказа Starbucks")
st.markdown("Введите параметры заказа и получите прогнозируемую выручку")

with st.form("prediction_form"):
    col1, col2 = st.columns(2)
    with col1:
        order_channel = st.selectbox("Канал заказа", ["Mobile App", "Drive-Thru", "Kiosk", "In-Store"])
        store_location_type = st.selectbox("Тип локации", ["Suburban", "Urban", "Rural"])
        region = st.selectbox("Регион", ["Northeast", "Midwest", "Southwest", "Southeast", "West"])
        customer_age_group = st.selectbox("Возрастная группа", ["18-24", "25-34", "35-44", "45-54", "55+"])
        customer_gender = st.selectbox("Пол", ["Male", "Female", "Prefer not to say"])
        is_rewards_member = st.checkbox("Участник программы лояльности")
        cart_size = st.number_input("Количество товаров", min_value=1, max_value=20, value=2, step=1)
        num_customizations = st.number_input("Количество кастомизаций", min_value=0, max_value=10, value=1)
    with col2:
        fulfillment_time_min = st.number_input("Время выполнения (мин)", min_value=0.0, max_value=60.0, value=5.0)
        drink_category = st.selectbox("Категория напитка", ["Brewed Coffee", "Espresso", "Frappuccino", "Refresher", "Tea", "Other"])
        has_food_item = st.checkbox("Есть еда")
        order_ahead = st.checkbox("Заказ заранее")
        customer_satisfaction = st.slider("Удовлетворённость (1-5)", 1, 5, 4)
        day_of_week_num = st.selectbox("День недели (0=Пн)", list(range(7)), index=0, format_func=lambda x: ["Пн","Вт","Ср","Чт","Пт","Сб","Вс"][x])
        hour = st.slider("Час дня", 0, 23, 12)
        time_period = st.selectbox("Время суток", ["morning", "afternoon", "evening", "night"])
        month = st.slider("Месяц", 1, 12, 6)
        day_of_month = st.slider("День месяца", 1, 31, 15)
        is_weekend = st.checkbox("Выходной")
    
    submitted = st.form_submit_button("Предсказать сумму")

if submitted:
    data = {
        "order_channel": order_channel,
        "store_location_type": store_location_type,
        "region": region,
        "customer_age_group": customer_age_group,
        "customer_gender": customer_gender,
        "is_rewards_member": is_rewards_member,
        "cart_size": cart_size,
        "num_customizations": num_customizations,
        "fulfillment_time_min": fulfillment_time_min,
        "drink_category": drink_category,
        "has_food_item": has_food_item,
        "order_ahead": order_ahead,
        "customer_satisfaction": customer_satisfaction,
        "day_of_week_num": day_of_week_num,
        "hour": hour,
        "time_period": time_period,
        "month": month,
        "day_of_month": day_of_month,
        "is_weekend": int(is_weekend)
    }
    try:
        response = requests.post("http://localhost:8000/predict", json=data, timeout=10)
        if response.status_code == 200:
            result = response.json()
            st.success(f"Прогнозируемая сумма заказа: **${result['predicted_total_spend']}**")
        else:
            st.error(f"Ошибка API: {response.text}")
    except requests.exceptions.ConnectionError:
        st.error("Не удалось подключиться к API. Запустите `python api.py` сначала.")
    except Exception as e:
        st.error(f"Ошибка: {e}")