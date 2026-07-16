import streamlit as st

from quantlab import (
    EuropeanOption,
    BlackScholes,
    MonteCarlo,
    delta,
    gamma,
    vega,
    implied_volatility,
)


st.title("Quapp")
st.write("Quantitative finance dashboard powered by QuantLab")


st.sidebar.header("Option Parameters")

spot = st.sidebar.number_input(
    "Spot Price",
    value=100.0
)

strike = st.sidebar.number_input(
    "Strike Price",
    value=100.0
)

maturity = st.sidebar.number_input(
    "Maturity (years)",
    value=1.0
)

rate = st.sidebar.number_input(
    "Risk-free Rate",
    value=0.05
)

volatility = st.sidebar.number_input(
    "Volatility",
    value=0.20
)


option = EuropeanOption(
    spot=spot,
    strike=strike,
    maturity=maturity,
    rate=rate,
    volatility=volatility,
)


bs = BlackScholes()
mc = MonteCarlo()


st.header("Pricing")

st.write(
    "Black-Scholes Price:",
    bs.price(option)
)

st.write(
    "Monte Carlo Price:",
    mc.price(option)
)


st.header("Greeks")

st.write(
    "Delta:",
    delta(option)
)

st.write(
    "Gamma:",
    gamma(option)
)

st.write(
    "Vega:",
    vega(option)
)


st.header("Volatility")

st.write(
    "Implied Volatility:",
    implied_volatility(
        bs.price(option),
        option
    )
)
