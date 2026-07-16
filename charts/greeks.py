import numpy as np
import plotly.graph_objects as go

from quantlab import delta, gamma, vega


def delta_vs_spot(option):

    spots = np.linspace(option.spot*0.5, option.spot*1.5, 100)

    values=[]

    for s in spots:
        temp=type(option)(
            spot=s,
            strike=option.strike,
            maturity=option.maturity,
            rate=option.rate,
            volatility=option.volatility,
        )

        values.append(delta(temp))


    fig=go.Figure()

    fig.add_trace(
        go.Scatter(
            x=spots,
            y=values,
            mode="lines",
            name="Delta",
            line=dict(color="green")
        )
    )

    fig.update_layout(
        title="Delta vs Spot"
    )

    return fig



def gamma_vs_spot(option):

    spots=np.linspace(option.spot*0.5, option.spot*1.5,100)

    values=[]

    for s in spots:
        temp=type(option)(
            spot=s,
            strike=option.strike,
            maturity=option.maturity,
            rate=option.rate,
            volatility=option.volatility,
        )

        values.append(gamma(temp))


    fig=go.Figure()

    fig.add_trace(
        go.Scatter(
            x=spots,
            y=values,
            mode="lines",
            name="Gamma",
            line=dict(color="red")
        )
    )

    fig.update_layout(
        title="Gamma vs Spot"
    )

    return fig



def vega_vs_volatility(option):

    vols=np.linspace(0.05,1,100)

    values=[]

    for v in vols:
        temp=type(option)(
            spot=option.spot,
            strike=option.strike,
            maturity=option.maturity,
            rate=option.rate,
            volatility=v,
        )

        values.append(vega(temp))


    fig=go.Figure()

    fig.add_trace(
        go.Scatter(
            x=vols,
            y=values,
            mode="lines",
            name="Vega",
            line=dict(color="purple")
        )
    )

    fig.update_layout(
        title="Vega vs Volatility"
    )

    return fig
