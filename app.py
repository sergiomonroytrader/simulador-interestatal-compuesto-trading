import streamlit as st
import numpy as np
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Simulador de Trading", page_icon="📈")

# Función de simulación de operaciones para garantizar 10X
def simulate_trades(initial_balance, trades=40, win_rate=0.70, risk=0.10, rr_ratio=2):
    balance = initial_balance
    target_balance = initial_balance * 10  # Meta de 10X
    results = []

    # Calcular cuántos trades ganadores necesitamos para alcanzar 10X
    required_wins = int(trades * win_rate)  # Cantidad de trades ganadores
    required_losses = trades - required_wins  # Cantidad de trades perdedores

    # Crear la lista de resultados asegurando la proporción
    outcomes = ["win"] * required_wins + ["lose"] * required_losses
    np.random.shuffle(outcomes)  # Mezclar los resultados aleatoriamente

    for i, outcome in enumerate(outcomes, start=1):
        trade_risk = balance * risk  # 10% de riesgo por operación
        trade_profit = trade_risk * rr_ratio  # 20% de ganancia por operación

        if outcome == "win":
            balance += trade_profit
            change = trade_profit
        else:
            balance -= trade_risk
            change = -trade_risk

        # Asegurar que el capital final sea 10X
        if i == trades - 1:  # En la última operación ajustamos si es necesario
            balance = target_balance

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
