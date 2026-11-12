# Getting fit uncertainties from an analytical Jacobian and comparing with curve_fit

## Link to the original question

https://discuss.python.org/t/104442

Nobody has posted the answer from this page at that link so any reader is free to carry the answer over to the person who asked.

One AI model (Claude) ran the test in a single chat on 12 November 2026 with scipy version 1.18.1 on made-up data and no other person has rerun the test yet which means the page is unconfirmed.

## The question

On 18 October 2025 somebody asked on the Python help forum for a light and fast least-squares method that gets the covariance matrix (the table of fit uncertainties) from analytical derivatives and wanted to compare the result with the covariance matrix that the scipy function curve_fit returns.
The post had zero replies when the forum list was read on 12 November 2026.

## What the test shows

The test fitted the model a·exp(−b·x) + c to 200 noisy points.
The Jacobian J is the table of derivatives of the model with respect to the three parameters at every data point.

- The covariance computed as s² times the inverse of (J transposed times J) with an analytical J matched the covariance from curve_fit to about 1 part in 100000. The number s² is the sum of squared leftovers divided by (number of points minus number of parameters).
- The standard errors were 0.015067 and 0.016543 and 0.006517 from both routes.
- The covariance from the full analytical Hessian (which adds second-derivative terms weighted by the leftovers) differed from curve_fit by about 2 percent.
- Passing the analytical Jacobian into curve_fit with the argument jac made 200 fits take 0.038 seconds against 0.052 seconds with numerical derivatives.

## Best-guess answer

The function curve_fit already builds the covariance from the Jacobian at the solution so the hand formula s² · inverse(Jᵀ J) reproduces the curve_fit result when the same Jacobian is used.
The lightest change is to keep curve_fit and pass the analytical Jacobian with jac= because curve_fit then uses exact derivatives for both the fit and the covariance.
A hand-built route is scipy.optimize.least_squares with jac= followed by the hand formula.
The full Hessian gives a slightly different covariance and the difference shrinks when the leftovers are small.

The test file named fit_uncertainty.py sits in boring-things inside research-program-files inside unanswered-questions-scripts.
