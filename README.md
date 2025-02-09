# Tests
We use Pytest to ensure the code is working as expected, by computing some well known limits, derivatives and integrals e check if the value is the expected value.
## Limits
Here are the limits and expected values used in the tests

Continuous functions
$$\lim_{x \rightarrow \, 1} x^2 = 1$$

$$\lim_{x \rightarrow \, \pi} \sin(x) = 0$$

Fundamental trigonometric limit
$$\lim_{x \rightarrow \, 0} \frac{\sin(x)}{x}  = 1$$

Limit to an accumulation point of the domain
$$\lim_{x \rightarrow \, 0} x \ln(x)  = 0$$

Lateral limits of a discontinuous function
$$ f(x) = \begin{cases} x^2 - x \,\, \text{if} \, x < 0 \\ e^x \,\, \text{if} \, x \ge 0 \end{cases} $$
$$\lim_{x \rightarrow \, 0^+} f(x)  = 1$$
$$\lim_{x \rightarrow \, 0^-} f(x)  = 0$$

Limit of a bounded function
$$ f(x) = \begin{cases} \sin(3x) \,\, \text{if} \, x \in \mathbb{Q} \\ x^2 + x \,\, \text{if} \, x \notin \mathbb{Q} \end{cases} $$
$$\lim_{x \rightarrow \, 0} f(x)  = 0$$

Bilateral limit of a discontinuous function
$$ f(x) = \begin{cases} x + \tan(x) \,\, \text{if} \, x \neq 0 \\ \pi + e \,\, \text{if} \, x = 0 \end{cases} $$
$$\lim_{x \rightarrow \, 0} f(x)  = 0$$
