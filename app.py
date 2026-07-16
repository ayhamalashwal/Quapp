from charts.pricing import (
    price_vs_spot,
    price_vs_volatility,
    price_vs_time,
)

from charts.greeks import (
    delta_vs_spot,
    gamma_vs_spot,
    vega_vs_volatility,
)

from charts.volatility import (
    implied_vol_curve,
)

from charts.monte_carlo import (
    monte_carlo_paths,
)
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


# -----------------------
# Page configuration
# -----------------------

st.set_page_config(
    page_title="Quapp",
    layout="wide",
)


# -----------------------
# Title
# -----------------------

st.title("Quapp")
st.caption(
    "Quantitative finance dashboard powered by QuantLab"
)


# -----------------------
# Sidebar Controls
# -----------------------

st.sidebar.header("Option Parameters")


spot = st.sidebar.slider(
    "Spot Price (S)",
    10.0,
    500.0,
    100.0,
    1.0
)


strike = st.sidebar.slider(
    "Strike Price (K)",
    10.0,
    500.0,
    100.0,
    1.0
)


maturity = st.sidebar.slider(
    "Maturity (Years)",
    0.05,
    10.0,
    1.0,
    0.05
)


rate = st.sidebar.slider(
    "Risk Free Rate (r)",
    0.0,
    0.20,
    0.05,
    0.005
)


volatility = st.sidebar.slider(
    "Volatility (σ)",
    0.01,
    1.0,
    0.20,
    0.01
)

# -----------------------
# Quant engine
# -----------------------

option = EuropeanOption(
    spot=spot,
    strike=strike,
    maturity=maturity,
    rate=rate,
    volatility=volatility,
)


bs = BlackScholes()
mc = MonteCarlo()


price = bs.price(option)
delta_value = delta(option)
gamma_value = gamma(option)
vega_value = vega(option)


# -----------------------
# Metrics
# -----------------------

st.subheader("Market Overview")


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Option Price",
        f"{price:.4f}"
    )


with col2:
    st.metric(
        "Delta",
        f"{delta_value:.4f}"
    )


with col3:
    st.metric(
        "Gamma",
        f"{gamma_value:.6f}"
    )


with col4:
    st.metric(
        "Vega",
        f"{vega_value:.4f}"
    )


# -----------------------
# Tabs
# -----------------------
pricing_tab, greeks_tab, volatility_tab, monte_tab = st.tabs(
    [
        "Pricing",
        "Greeks",
        "Volatility",
        "Monte Carlo",
    ]
)


# -----------------------
# Pricing
# -----------------------

with pricing_tab:

    st.header("Option Pricing Analysis")

    st.plotly_chart(
        price_vs_spot(option, bs),
        use_container_width=True
    )

    st.plotly_chart(
        price_vs_volatility(option, bs),
        use_container_width=True
    )

    st.plotly_chart(
        price_vs_time(option, bs),
        use_container_width=True
    )


# -----------------------
# Greeks
# -----------------------

with greeks_tab:

    st.header("Risk Sensitivities")

    st.plotly_chart(
        delta_vs_spot(option),
        use_container_width=True
    )

    st.plotly_chart(
        gamma_vs_spot(option),
        use_container_width=True
    )

    st.plotly_chart(
        vega_vs_volatility(option),
        use_container_width=True
    )


# -----------------------
# Volatility
# -----------------------

with volatility_tab:

    st.header("Volatility Analysis")

    st.plotly_chart(
        implied_vol_curve(option, bs),
        use_container_width=True
    )


# -----------------------
# Monte Carlo
# -----------------------

with monte_tab:

    st.header("Monte Carlo Simulation")

    st.plotly_chart(
        monte_carlo_paths(option),
        use_container_width=True
    )
