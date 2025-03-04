import streamlit as st
import numpy as np
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Simulador de Trading", page_icon="📈")

# Función de simulación de operaciones con orden específico para alcanzar 10X
def simulate_trades(initial_balance, trades=40, risk=0.10, rr_ratio=2):
    balance = initial_balance
    results = []
    
    # Orden específico de operaciones para alcanzar un resultado cercano a 10X
    outcomes = [
        "win", "win", "lose", "win", "win", "win", "lose", "win", "win", "win",
        "lose", "win", "win", "win", "win", "lose", "win", "win", "win", "lose",
        "win", "win", "win", "win", "lose", "win", "win", "win", "win", "win",
        "lose", "win", "win", "win", "win", "win", "win", "win", "lose", "win"
    ]  # Patrón específico para que el capital crezca cercano a 10X
    
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
st.title("📊 Simulador de Trading - Método Monroy")

initial_balance = st.number_input("💰 Ingresa tu capital inicial:", min_value=10, value=1000, step=10)

simulate = st.button("🚀 Simular Operaciones")

if simulate:
    df_results = simulate_trades(initial_balance)
    st.subheader("📈 Resultados de las 40 Operaciones")
    st.dataframe(df_results)  # Mostrar los datos en la app
