import streamlit as st
import numpy as np
import pandas as pd

def simulate_trades(initial_balance, trades=30, win_rate=0.70, risk=0.05, rr_ratio=2):
    balance = initial_balance
    results = []
    outcomes = np.random.choice(["win", "lose"], size=trades, p=[win_rate, 1 - win_rate])

    for i, outcome in enumerate(outcomes, start=1):
        trade_risk = balance * risk
        trade_profit = trade_risk * rr_ratio

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

st.title("📊 Simulador de Trading - 70% de Efectividad")
initial_balance = st.number_input("💰 Ingresa tu capital inicial:", min_value=10, value=1000, step=10)
if st.button("🚀 Simular Operaciones"):
    df_results = simulate_trades(initial_balance)
    st.write("## 📈 Resultados de las
