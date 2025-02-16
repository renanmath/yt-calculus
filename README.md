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

## Derivatives

Derivative of quadratic function
$$ \frac{d}{dx} \left( x^2 \right) \Big|_{x=0} = 0 $$

Derivative of a quintic function
$$ \frac{d}{dx} \left( x^5 - 2x^4 + 3x^3 - 4x^2 + 5x - 6 \right) \Big|_{x=1} = 3 $$

Derivative of sine function
$$ \frac{d}{dx} \left( \sin(2x) \right) \Big|_{x=0} = 2 $$

Derivative of tangent function
$$ \frac{d}{dx} \left( \tan(x) \right) \Big|_{x=\pi/6} = \frac{4}{3} $$

Derivative of logarithm function
$$ \frac{d}{dx} \left( \ln(x) \right) \Big|_{x=13} = \frac{1}{13} $$

Derivative of square root function
$$ \frac{d}{dx} \left( \sqrt{x} \right) \Big|_{x=2} = \frac{\sqrt{2}}{4} $$

Derivative of product of functions
$$ \frac{d}{dx} \left( x^2 \ln(x) \right) \Big|_{x=e} = 3e $$

Derivative of quotient of functions
$$ \frac{d}{dx} \left( \frac{x}{e^x} \right) \Big|_{x=0} = 1 $$

Derivative of composite functions
$$ \frac{d}{dx} \left( e^{\sin(x)} \right) \Big|_{x=0} = 1 $$
$$ \frac{d}{dx} \left( \sin(\pi e^x) \right) \Big|_{x=\ln(2)} = 2\pi $$

Module function is continuous but not differentiable
$$ \nexists \,\, \frac{d}{dx} \left( |x| \right) \Big|_{x=0} $$

Discontinuous function is not differentiable
$$ f(x) = \begin{cases} x^2 \,\, \text{if} \, x \neq 0 \\ 1 \,\, \text{if} \, x = 0 \end{cases} $$
$$ \nexists \,\, \frac{d}{dx} \left( f(x) \right) \Big|_{x=0} $$


## Integrals


Integral of identity function
$$ \int_{0}^{3} x dx = \frac{9}{2} $$

Integral of quadratic function
$$ \int_{0}^{1} x^2 + 1 \, dx = \frac{4}{3} $$

Integral of odd function in symmetrical interval
$$ \int_{-1}^{1} x^3 - 3x \, dx = 0 $$

Integral of cosine function
$$ \int_{\pi/2}^{\pi} \cos(x) \, dx = -1 $$

Integral of exponential function
$$ \int_{0}^{\ln(3)} e^x \, dx = 2 $$

Integral of logarithm function (integration by parts)
$$ \int_{1}^{e^2} \ln(x) \, dx = e^2 + 1 $$

Integral of rational function (integration by substitution)
$$ \int_{1}^{2} \frac{1}{x+1} \, dx = \ln(\frac{3}{2}) $$

Integral of cosine identities
$$ \int_{0}^{\pi} \cos(x)^2 \, dx = \frac{\pi}{2} $$
$$ \int_{0}^{\pi} \cos(2x)\cos(3x) \, dx = 0 $$

Integral of interesting power
$$ \int_{0}^{1} x^{-x}(1-x)^{x-1}\sin(\pi x) \, dx = \frac{\pi}{e} $$

Sophomore's Dream Identities
$$ \int_{0}^{1} x^{-x} \, dx = \sum_{n=1}^{\infty} n^{-n} \approx 1.29128599706266 $$
$$ \int_{0}^{1} x^{x} \, dx = \sum_{n=1}^{\infty} (-1)^{n+1}n^{-n} \approx 0.78343051071213 $$
