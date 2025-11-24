# Math → Coding

## 1. Linear Algebra

### 1.1 Vectors, Matrices, and Matrix Operations

A simple Python project demonstrating vector and matrix operations using NumPy, including:
- Vector creation and properties
- Matrix creation and basic operations (addition, subtraction, multiplication)
- Transpose, inverse, identity, and diagonal matrices

### 1.2 Eigenvalues, Eigenvectors, Norm and Projections

Implementing and understanding fundamental linear algebra operations using NumPy: 
- Dot product and Matrix multiplication
- Computing Eigenvalues and Eigenvectors
- Understanding computations of Norm and Projections 

### 1.3 Matrix Decomposition (SVD, PCA Basics)

Implementing and understanding matrix factorization techniques and dimensionality reduction using NumPy:

#### Singular Value Decomposition (SVD).
- Factorizes a matrix into: U (left vectors), S (singular values), Vᵀ (right vectors)
- Useful for compression, noise removal, and understanding matrix structure.

#### PCA Basics Using SVD
- Center the data
- Apply SVD
- Take top principal components from Vᵀ
- Project data into lower dimension

## Calculus

### 2.1 Derivatives and Partial Derivatives, Gradient and Gradient Descent
Understanding how functions change using derivatives and gradients, and applying gradient descent for basic optimization tasks using SymPy: 
- Compute derivatives and partial derivatives to see how functions change.
- Use gradients to find directions of steepest change.
- Apply gradient descent to minimize a loss function and optimize weights in machine learning.

### 2.2  Chain Rule
Understanding how changes in weights affect the output and loss in a simple neural network:
- Manually compute the forward pass, loss, and backpropagation steps to find how the loss changes with respect to the weight.
- Understand how activation, chain rule, and gradients combine to update parameters in simple neural networks.

## Probability 

### 3.1 Probability basics and Conditional Probability 
Exploring descriptive statistics and basic probability concepts to analyze simple datasets:
- Compute key statistical measures: mean, median, mode, and standard deviation.
- Analyze binary datasets to find probabilities of individual events.
- Calculate joint probability to understand how two events occur together.
- Use conditional probability to measure how one event affects the likelihood of another.

### 3.2 Bayes' Theorem, Random variables and Distributions
Understanding uncertainty through Bayes' rule and generating data from different probability distributions:
- Apply Bayes’ theorem to update beliefs using prior, likelihood, and evidence.
- Generate Bernoullis samples to simulate single yes/no outcomes.
- Generate Binomial samples to model repeated trials with fixed probability of success.
- Generate Normal distribution samples to observe data drawn from a bell-shaped distribution.

### 3.3 Likelihood, Correlation, Hypothesis Testing & Cross-Entropy
Understanding statistical reasoning used in ML through probability, relationships between variables, model comparison, and loss functions:
- Compute likelihood of coin-flip data for different probability values.
- Calculate covariance and correlation to measure how two variables move together.
- Perform a t-test to compare two model accuracy distributions.
- Compute cross-entropy loss to evaluate prediction confidence for the true class.
