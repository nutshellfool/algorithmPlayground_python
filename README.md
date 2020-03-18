# algorithm Playground for Python

[![Build Status](https://travis-ci.org/nutshellfool/algorithmPlayground_python.svg?branch=master)](https://travis-ci.org/nutshellfool/algorithmPlayground_python)
 
This is a Python edition, and Java edition is also available [algorithmPlayground](https://github.com/nutshellfool/algorithmPlayground).   
Currently, this is a pure Python project and which supports the PyCharm IDE , so you can feel free to open this project in Python.  
The unittest is using build-in unittest (maybe change this in future),  and you can run all test-cases by   
```python -m unittest discover -s ./tests ``` (of course, you should run this command under the root path of this project)  
about the coverage under Python project:  
to gathering and report the coverage measurement, we can install [coverage package](https://github.com/nedbat/coveragepy).  
install package:  
```BASH
pip install coverage
```  
run test suites and gathering coverage information:  
```BASH
coverage run -m unittest discover
```
show the coverage report:  
```BASH
coverage report -m
```
to see more usage please refer [coverage docs](https://coverage.readthedocs.io/en/stable/)

## Algorithm & Data Structure problem / solution sets

### Array & Linked List

- [ ] [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)  
- [ ] [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- [x] [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [ ] [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
- [ ] [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [ ] [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [ ] [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [x] [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [x] [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)

### Stack & Queue

- [ ] [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [ ] [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [ ] [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

### Skip-list

### HashMap & Set

- [ ] [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [ ] [Two Sum](https://leetcode.com/problems/two-sum/)
- [ ] [3Sum](https://leetcode.com/problems/3sum/)
- [ ] [4Sum](https://leetcode.com/problems/4sum/)

- [ ] [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [ ] [Majority Element](https://leetcode.com/problems/majority-element/)

### Tree - Binary Search Tree

- [ ] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [ ] [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [ ] [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [ ] [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [ ] [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [ ] [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

### Priority Queue(heap)

- [ ] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [ ] [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [ ] [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [ ] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [ ] [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

### Binary Search

- [ ] [Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [ ] [Sqrt(x)](https://leetcode.com/problems/sqrtx/)

### Breath First Search

- [ ] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [ ] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

### Depth First Search

- [ ] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [ ] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [ ] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

## Basic algorithm thinking

### Recursion

- [ ] [Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [ ] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

### Divide & Conquer

- [ ] [Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [ ] [Majority Element](https://leetcode.com/problems/majority-element/)
- [ ] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [ ] [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

### Greedy

### Backtracking

### Dynamic Programming

- [ ] [Fibonacci Number](https://leetcode.com/problems/fibonacci-number/)
- [ ] [Climbing Stairs](https://leetcode.com/problems/climbing-stairs/)
- [ ] [Edit Distance](https://leetcode.com/problems/edit-distance/)
- [ ] [Triangle](https://leetcode.com/problems/triangle/)
- [ ] [Maximum Product Subarray](https://leetcode.com/problems/maximum-product-subarray/)
- [ ] [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
- [ ] [Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)
- [ ] [Best Time to Buy and Sell Stock III](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)
- [ ] [Best Time to Buy and Sell Stock IV](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/)
- [ ] [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)
- [ ] [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
- [ ] [Longest Increasing Subsequence](https://leetcode.com/problems/longest-increasing-subsequence/)
- [ ] [Coin Change](https://leetcode.com/problems/coin-change/)

## Advanced data structure & algorithm

### trie Tree

- [ ] [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

### Union-find

- [ ] [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [ ] [Friend Circles](https://leetcode.com/problems/friend-circles/)

### Bitmap

### Bloom-filter

### Bitwise

- [ ] [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [ ] [Power of Two](https://leetcode.com/problems/power-of-two/)
- [ ] [Counting Bits](https://leetcode.com/problems/counting-bits/)

## System design Problem / Solution sets

### Basic components

#### cache

##### LRU Cache

- [ ] [LRU Cache](https://leetcode.com/problems/lru-cache/)
