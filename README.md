# Create_Decision_Tree-Gini-Index-
Code to implement the first step of a Decision Tree class.
In this assignment, we will implement the first step of a Decision Tree class. You are
not being asked to implement a full Decision Tree, just the first step.
Given a dataset of items and labels, we can learn a Decision Tree in order to perform classification. We will consider a binary tree, where at each node we must find the best partition that minimizes the Gini index. For this assignment, you must create a DecisionTree class, and a method that finds the partition (“split”) with the minimum Gini index. You do not need to im- plement the full Decision Tree training, but just the method that finds the best split of a dataset. Your method must return the splitting point, and the two new datasets created.
We will consider here that each item has a single continuous feature and a label. We will also consider only two labels: 0 or 1. As usual, you should test all midpoints of continuous features. Only the test x ≤ y will be used, where x is the value of the feature for the current item and y is a possible splitting point.
Therefore, your method must return the value y that minimizes the Gini index, and two datasets: left, where x ≤ y, ∀x; and right, where x > y, ∀x.
