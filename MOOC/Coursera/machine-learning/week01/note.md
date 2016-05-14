# introduction 

Machine learning:
* Grew out of work in AI
* New capability for computers

Examples:
* Database Mining
Large datasets from growth of automation / web. E.g. web click data, medical records, biology, engineering.

* Application can't program by hand. E.g. Autonomous helicopter, handwriting recognition, most of Natural Language Processing (NLP), Computer Vision.

* Self-customizing programs. E.g., Amazon, Netflix product recommendations.

* Understanding human learning (brain, real AI)

## Supervised Learning
Example 1: housing price prediction (__regression__) -> "right answers" given

Example 2: breast cancer (malignant, benign) (__classification__, discrete valued output)

__Support Vector Machine__ -> dealing with infinity features 

## Unsupervised Learning
There are no labels, find structures for us.

Example: Google News (__Clustering__)

Example: Genes clustering

Applications: Organize computing clusters, social network analysis, market segmentation, astronomical data analysis.

Example: Cocktail party problem
One line code
```matlab
[W, s, v] = svd((repmat(sum(x.*x, 1), size(x, 1), 1).*x)*x');
```

svd: singular value decomposition
repmat: repeat copies of array

Using [__Octave__](https://www.gnu.org/software/octave/).



# Model and Cost Function

Linear regression predicts a real-valued output based on an input value. We discuss the application of linear regression to housing price prediction, present the notion of a cost function, and introduce the gradient descent method for learning.

## Model representation
Example: housing prices prediction 

__Supervised learning__: given the "right answer" for each example in the data.

* Regression problem: predict real valued output
* Classification problem: discrete valued output


Notation:  
__m__ = Number of training examples  
__x's__ = input variable/ features  
__y's__ = output variable/ target variable  
__(x, y)__ = single training example  
__(x(i), y(i))__ = ith training example  

Processing:  
Training set -> learning algorithm -> h(hypothesis) -> estimated price  
__h__ is a map from x's to y's

Represent h:  
$$ h_\theta(x) = \theta_0 + \theta_1 x $$

## Cost Function
$$ \theta_0, \theta_1 $$ are parameters

Squared error function:  
$$ J(\theta_0, \theta_1) = \text{min} \frac{1}{2m} \sum^{m}_{i=1} (h_\theta(x^(i)) - y^(i))^2 $$ 

## Cost Function - intuition 1

Two functions $$ h_{\theta}(x), J(\theta_1) $$

## Cost Function - intuition 2

contour plot (contour figure)

# Parameter Learning

## Gradient Descent
Outline:
* start with some \theta_0, \theta_1
* keep changing \theta_0, \theta_1 to reduce J(\theta_0, \theta_1) until we hopefully end up at a minimum.

Gradient descent algorithm  
Simultaneous update is import !!! 

## Gradient Descent Intuition
\alpha : learning rate  
derivative term  

\alpha is too small -> gradient descent can be slow  
\alpha is too large -> gradient descent can overshoot the minimum, it may fail to converge, or even diverge  

fixed \alpha will lead gradient descent  automatically take smaller steps, no need to decrease \alpha over time


## Gradient Descent For Linear Regression
apply gradient descent algorithm to linear regression  
cost function is a __convex function__  

batch gradient descent: each step of gradient descent uses all the training examples


# Linear Algebra Review (Skipping)

## Matrices and Vectors

## Addition and Scalar Multiplication

## Matrix Vector Multiplication

## Matrix Matrix Multiplication

## Matrix Multiplication Properties

## Inverse and Transpose

