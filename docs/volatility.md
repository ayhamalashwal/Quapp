# Volatility Tools

QuantLab provides tools for analyzing volatility, including implied volatility calculation.

---

# Implied Volatility

## Definition

Implied volatility is the volatility value that makes a theoretical option price equal to the observed market price.

Normal option pricing works like this:

```
Volatility → Option Price
```

For example:

```
20% volatility → $10.45 option price
```

Implied volatility reverses this process:

```
Market Price → Implied Volatility
```

---

# Why Implied Volatility Matters

Unlike stock prices, volatility is not directly observable.

The market does not tell us:

```
"The volatility is 20%"
```

Instead, we observe:

```
"The option is trading at $10.45"
```

and solve for the volatility that explains this price.

---

# Mathematical Formulation

The problem is solved by finding:

$$
BS(\sigma)-MarketPrice=0
$$

Where:

- \(BS(\sigma)\) is the Black-Scholes price using volatility \(\sigma\)
- MarketPrice is the observed option price

The goal is to find the volatility value where both prices match.

---

# Numerical Method

QuantLab uses Brent's method to solve for implied volatility.

The algorithm:

1. Choose a range of possible volatility values
2. Calculate the Black-Scholes price
3. Compare with market price
4. Adjust volatility
5. Repeat until the difference approaches zero

---

# Example

```python
from quantlab import implied_volatility

market_price = 10.45

volatility = implied_volatility(
    market_price,
    option
)

print(volatility)
```

Output:

```
0.20
```

Meaning the market price implies approximately:

```
20% volatility
```

---

# Applications

Implied volatility is used in:

- Options trading
- Volatility forecasting
- Risk management
- Comparing option prices across markets
- Building volatility surfaces
