# Option Greeks

Option Greeks measure how sensitive an option's price is to changes in different market variables.

They are essential for:

- Risk management
- Hedging
- Portfolio analysis
- Understanding option behavior

QuantLab currently supports:

- Delta
- Gamma
- Vega

---

# Delta

## Definition

Delta measures the sensitivity of an option price to changes in the underlying asset price.

Mathematically:

$$
\Delta = \frac{\partial C}{\partial S}
$$

For a European call option:

$$
\Delta = N(d_1)
$$

where \(N\) is the cumulative normal distribution.

---

## Interpretation

A Delta of:

```
0.63
```

means:

If the stock price increases by $1:

```
Option price increases approximately by $0.63
```

---

## Uses

Delta is used for:

- Measuring directional exposure
- Creating delta-neutral portfolios
- Hedging option positions

Example:

```python
from quantlab import delta

delta_value = delta(option)
```

---

# Gamma

## Definition

Gamma measures how quickly Delta changes when the underlying asset price changes.

Mathematically:

$$
\Gamma = \frac{\partial^2 C}{\partial S^2}
$$

Gamma is the second derivative of option price with respect to the underlying price.

---

## Interpretation

A high Gamma means:

- Delta changes rapidly
- The option is more sensitive to market movements
- Hedging needs more frequent adjustment

Gamma is usually highest when:

- The option is near the strike price
- The expiration date is close

Example:

```python
from quantlab import gamma

gamma_value = gamma(option)
```

---

# Vega

## Definition

Vega measures sensitivity to changes in volatility.

Mathematically:

$$
\nu = \frac{\partial C}{\partial \sigma}
$$

where \(\sigma\) represents volatility.

---

## Interpretation

If Vega is:

```
37.5
```

then a 1% increase in volatility changes the option price approximately by:

```
0.01 × 37.5 = 0.375
```

---

## Importance

Volatility is one of the most important factors in option pricing.

Vega is used for:

- Volatility trading
- Risk management
- Understanding implied volatility changes

Example:

```python
from quantlab import vega

vega_value = vega(option)
```

---

# Summary

| Greek | Measures | Sensitivity |
|------|----------|-------------|
| Delta | Directional exposure | Stock price |
| Gamma | Delta change | Stock price movement |
| Vega | Volatility exposure | Implied volatility |

QuantLab calculates these values using the Black-Scholes framework.
