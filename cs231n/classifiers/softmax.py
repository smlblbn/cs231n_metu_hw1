import numpy as np
from random import shuffle

def softmax_loss_naive(W, X, y, reg):
  """
  Softmax loss function, naive implementation (with loops)
  Inputs:
  - W: C x D array of weights
  - X: D x N array of data. Data are D-dimensional columns
  - y: 1-dimensional array of length N with labels 0...K-1, for K classes
  - reg: (float) regularization strength
  Returns:
  a tuple of:
  - loss as single float
  - gradient with respect to weights W, an array of same size as W
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using explicit loops.     #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_classes = W.shape[0]
  num_train = X.shape[1]
  X = X.T

  for i in range(num_train):
    scores = np.dot(W, X[i])
    sum_exp = np.sum(np.exp(scores))
    loss += np.log(sum_exp) - scores[y[i]]

    for j in range(num_classes):
      dW[j] += (np.exp(scores[j]) / sum_exp) * X[i]
    dW[y[i]] -= X[i]

  dW /= num_train
  dW += reg * W

  loss /= num_train
  loss += (0.5 * reg) * np.sum(W**2)
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW


def softmax_loss_vectorized(W, X, y, reg):
  """
  Softmax loss function, vectorized version.

  Inputs and outputs are the same as softmax_loss_naive.
  """
  # Initialize the loss and gradient to zero.
  loss = 0.0
  dW = np.zeros_like(W)

  #############################################################################
  # TODO: Compute the softmax loss and its gradient using no explicit loops.  #
  # Store the loss in loss and the gradient in dW. If you are not careful     #
  # here, it is easy to run into numeric instability. Don't forget the        #
  # regularization!                                                           #
  #############################################################################
  num_train = X.shape[1]

  product = np.dot(W, X).T
  expected = np.exp(product) / np.sum(np.exp(product), axis=1, keepdims=True)

  loss = np.sum(-np.log(expected[np.arange(num_train), y])) / num_train
  loss += (0.5 * reg) * np.sum(W**2)

  tmp = np.zeros_like(expected)
  tmp[np.arange(num_train), y] = 1

  dW = np.dot(X, (expected - tmp)).T / num_train
  dW += reg * W
  #############################################################################
  #                          END OF YOUR CODE                                 #
  #############################################################################

  return loss, dW
