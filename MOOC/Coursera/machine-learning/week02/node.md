# Linear Regression with Multiple Variables

## Envionment Setup Instructions

install Octave on Linux
```bash
sudo apt-get install octave
```

## Multivariate Linear Regression

### Multiple Features
Notation:  
n -> number of features  
x_0 = 1  

feature vector & parameter vector will be n+1

### Gradient Descent for Multiple Variables

### Gradient Descent in Practice - Feature Scaling

### Gradient Descent in Practice - learning rate
J(\theta) should decrease after every iteration

if \alpha is too small: slow convergence  
if \alpha is too large: J(\theta) may not decrease on every iteration; may not converge (slow converge also possible)

### Features and Polynomial Regression

In polynomial regression, feature scaling will be important.

## Computer Parameters Analtically

### Normal Equation
Method to solve for \theta analytically

$$ \theta = (X^T X)^{-1} X^T y $$

```octave
pinv(x'*x)*x'*y
```

Gradient Descent
* need to choose \alpha
* Need many iterations
* Works well even when n is large

Normal Equation
* no need to change \alpha
* don't need to iterate
* need to computer inverse, slow if n is large

### Normal Equation - noninvertbility
* redundant features  
* too many features -> regularization

# Octave/Matlab Tutorial

## Octave/Matlab Tutorial