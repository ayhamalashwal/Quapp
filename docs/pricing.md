# Option Pricing

QuantLab currently supports two pricing methods:

- Black-Scholes analytical pricing
- Monte Carlo simulation pricing

---

# Black-Scholes Model

The Black-Scholes model provides a closed-form solution for pricing European options.

For a European call option:

$$
C = S_0N(d_1)-Ke^{-rT}N(d_2)
$$

Where:

- \(S_0\): current underlying asset price
- \(K\): strike price
- \(T\): time until expiration
- \(r\): risk-free interest rate
- \(\sigma\): volatility
- \(N(x)\): cumulative normal distribution

The intermediate variables are:

$$
d_1 =
\frac{
\ln(S_0/K)+(r+\sigma^2/2)T
}{
\sigma\sqrt{T}
}
$$

$$
d_2=d_1-\sigma\sqrt{T}
$$

## Assumptions

The Black-Scholes model assumes:

- Constant volatility
- Log-normal asset price distribution
- No transaction costs
- Continuous trading
- European exercise only

## Implementation

Example:

```python
option = EuropeanOption(
    spot=100,
    strike=100,
    maturity=1,
    rate=0.05,
    volatility=0.2
)

price = BlackScholes().price(option)
```

---

# Monte Carlo Pricing

Monte Carlo pricing estimates option value through simulation.

Instead of solving a formula, it creates thousands of possible future prices.

The process:

1. Generate random market scenarios
2. Calculate option payoff for each scenario
3. Average the payoffs
4. Discount back to present value

The estimated price is:

$$
Price=e^{-rT}E[Payoff]
$$

## Advantages

- Flexible
- Works for complex derivatives
- Easy to extend

## Disadvantages

- Slower than analytical methods
- Requires many simulations for accuracy
