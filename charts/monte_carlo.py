import numpy as np
import plotly.graph_objects as go


def monte_carlo_paths(option, simulations=50):

    paths = []

    for _ in range(simulations):

        prices = [option.spot]

        for _ in range(100):

            change = np.random.normal(
                0,
                option.volatility / np.sqrt(100)
            )

            prices.append(
                prices[-1] * (1 + change)
            )

        paths.append(prices)


    fig = go.Figure()

    for path in paths:
        fig.add_trace(
            go.Scatter(
                y=path,
                mode="lines",
                showlegend=False
            )
        )

    fig.update_layout(
        title="Monte Carlo Price Paths",
        xaxis_title="Time",
        yaxis_title="Price"
    )

    return fig
