import numpy as np
import plotly.graph_objects as go

from quantlab import implied_volatility


def implied_vol_curve(option, model):

    base_price = model.price(option)

    prices = np.linspace(
        max(0.01, base_price * 0.8),
        base_price * 1.2,
        50
    )

    vols = []

    valid_prices = []

    for p in prices:
        try:
            vol = implied_volatility(
                p,
                option
            )

            vols.append(vol)
            valid_prices.append(p)

        except ValueError:
            continue


    fig = go.Figure()


    fig.add_trace(
        go.Scatter(
            x=valid_prices,
            y=vols,
            mode="lines",
            name="Implied Volatility",
            line=dict(color="orange")
        )
    )


    fig.update_layout(
        title="Implied Volatility Curve",
        xaxis_title="Option Price",
        yaxis_title="Implied Volatility"
    )


    return fig
