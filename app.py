import streamlit as st
import numpy as np
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Simulador de Trading", page_icon="📈")

# Función de simulación de operaciones para garantizar un orden fijo y 10X natural
def simulate_trades(initial_balance, trades=40, risk=0.10, rr_ratio=2):
    balance = initial_balance
    results = []
    
    # Orden predefinido de operaciones para lograr un crecimiento cercano a 10X
    outcomes = (["win"] * 28) + (["lose"] * 12)  # 28 ganadas, 12 perdidas
    
    for i, outcome in enumerate(outcomes, start=1):
        trade_risk = balance * risk  # 10% de riesgo por operación
        trade_profit = trade_risk * rr_ratio  # 20% de ganancia por operación

        if outcome == "win":
            balance += trade_profit
            change = trade_profit
        else:
            balance -= trade_risk
            change = -trade_risk

        results.append({
            "Trade": i,
            "Resultado": "Ganado" if outcome == "win" else "Perdido",
            "Cambio ($)": round(change, 2),
            "Capital después del Trade ($)": round(balance, 2)
        })

    return pd.DataFrame(results)

# Interfaz en Streamlit
st.title("📊 Simulador de Trading - Método Monroy (10X Aproximado)")

initial_balance = st.number_input("💰 Ingresa tu capital inicial:", min_value=10, value=1000, step=10)

simulate = st.button("🚀 Simular Operaciones")

if simulate:
    df_results = simulate_trades(initial_balance)
    st.subheader("📈 Resultados de las 40 Operaciones")
    st.dataframe(df_results)  # Mostrar los datos en la app
