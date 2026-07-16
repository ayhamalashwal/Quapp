import numpy as np
import matplotlib.pyplot as plt


def price_vs_spot(option, model):

    spots = np.linspace(
        option.spot * 0.5,
        option.spot * 1.5,
        100
    )

    prices = []

    for s in spots:
        temp_option = type(option)(
            spot=s,
            strike=option.strike,
            maturity=option.maturity,
            rate=option.rate,
            volatility=option.volatility,
        )

        prices.append(
            model.price(temp_option)
        )

    fig, ax = plt.subplots()

    ax.plot(spots, prices)

    ax.set_xlabel("Spot Price")
    ax.set_ylabel("Option Price")
    ax.set_title("Option Price vs Spot Price")

    return fig
