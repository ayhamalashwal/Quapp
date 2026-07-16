import numpy as np
import plotly.graph_objects as go


def price_vs_spot(option, model):

    spots = np.linspace(
        option.spot * 0.5,
        option.spot * 1.5,
        100
    )

    prices = []

    for s in spots:
        temp = type(option)(
            spot=s,
            strike=option.strike,
            maturity=option.maturity,
            rate=option.rate,
            volatility=option.volatility,
        )

        prices.append(model.price(temp))


    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=spots,
            y=prices,
            mode="lines",
            name="Price",
            line=dict(color="royalblue")
        )
    )

    fig.update_layout(
        title="Option Price vs Spot",
        xaxis_title="Spot Price",
        yaxis_title="Option Price"
    )

    return fig



def price_vs_volatility(option, model):

    vols = np.linspace(0.05, 1, 100)

    prices = []

    for v in vols:
        temp = type(option)(
            spot=option.spot,
            strike=option.strike,
            maturity=option.maturity,
            rate=option.rate,
            volatility=v,
        )

        prices.append(model.price(temp))


    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=vols,
            y=prices,
            mode="lines",
            name="Price",
            line=dict(color="orange")
        )
    )

    fig.update_layout(
        title="Option Price vs Volatility",
        xaxis_title="Volatility",
        yaxis_title="Option Price"
    )

    return fig



def price_vs_time(option, model):

    times = np.linspace(0.05, 5, 100)

    prices = []

    for t in times:
        temp = type(option)(
            spot=option.spot,
            strike=option.strike,
            maturity=t,
            rate=option.rate,
            volatility=option.volatility,
        )

        prices.append(model.price(temp))


    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=times,
            y=prices,
            mode="lines",
            name="Price",
            line=dict(color="purple")
        )
    )

    fig.update_layout(
        title="Option Price vs Time",
        xaxis_title="Years",
        yaxis_title="Option Price"
    )

    return fig
