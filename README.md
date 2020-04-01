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

### Array

- [x] [Container With Most Water](https://leetcode.com/problems/container-with-most-water)
- [x] [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- [ ] [Maximum Swap](https://leetcode.com/problems/maximum-swap/)

###Linked List

- [x] [Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)  
- [x] [Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)
- [x] [Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/)
- [ ] [Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)
- [x] [Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)
- [ ] [Reverse Nodes in k-Group](https://leetcode.com/problems/reverse-nodes-in-k-group/)
- [x] [Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)
- [x] [Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/)
- [x] [Merge k Sorted Lists](https://leetcode.com/problems/merge-k-sorted-lists/)
- [x] [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)
- [x] [Add Two Numbers II](https://leetcode.com/problems/add-two-numbers-ii/)
- [ ] [Reorder List](https://leetcode.com/problems/reorder-list/)


### Stack & Queue

- [x] [Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)
- [ ] [Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)
- [ ] [Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

### Deque

- [x] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)

### Skip-list

### HashMap & Set

- [x] [Valid Anagram](https://leetcode.com/problems/valid-anagram/)
- [x] [Two Sum](https://leetcode.com/problems/two-sum/)
- [x] [3Sum](https://leetcode.com/problems/3sum/)
- [x] [4Sum](https://leetcode.com/problems/4sum/)

- [x] [Two Sum II - Input array is sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)
- [x] [Majority Element](https://leetcode.com/problems/majority-element/)

### Tree - Binary Search Tree

- [x] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [x] [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [x] [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [x] [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [x] [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [x] [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

### Priority Queue(heap)

- [x] [Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/)
- [x] [Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)
- [x] [Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/)
- [x] [Find Median from Data Stream](https://leetcode.com/problems/find-median-from-data-stream/)
- [x] [Sliding Window Median](https://leetcode.com/problems/sliding-window-median/)

**possible**
- [ ] [Lexicographical Numbers](https://leetcode.com/problems/lexicographical-numbers/)
- [ ] [K-th Smallest in Lexicographical Order](https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/)

### Binary Search

- [x] [Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [x] [Sqrt(x)](https://leetcode.com/problems/sqrtx/)
- [x] [Divide Two Integers](https://leetcode.com/problems/divide-two-integers/)
- [ ] [Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)
- [ ] [Gas Station](https://lintcode.com/problem/gas-station)

### Breadth First Search

- [x] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [x] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [x] [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [ ] [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

### Depth First Search

- [x] [Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)
- [x] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [x] [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)
- [ ] [Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

## Basic algorithm thinking

### Recursion

- [x] [Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [x] [Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)
- [x] [Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)
- [x] [Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)
- [x] [Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/)
- [x] [Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/)
- [x] [Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)
- [x] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [x] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)

### Divide & Conquer

- [x] [Pow(x, n)](https://leetcode.com/problems/powx-n/)
- [ ] [Majority Element](https://leetcode.com/problems/majority-element/)
- [x] [Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/)
- [x] [Minimum Depth of Binary Tree](https://leetcode.com/problems/minimum-depth-of-binary-tree/)

### Greedy

- [ ] [Candy](https://leetcode.com/problems/candy/)
- [ ] [Divide Chocolate](https://leetcode-cn.com/problems/divide-chocolate/)

### Backtracking
- [x] [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [ ] [Restore IP Addresses](https://leetcode.com/problems/restore-ip-addresses/)
- [ ] [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/)

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
- [x] [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)
- [ ] [Android Unlock Patterns](https://leetcode.com/problems/android-unlock-patterns/)

## Advanced data structure & algorithm

### trie Tree

- [ ] [Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)

### Union-find

- [ ] [Number of Islands](https://leetcode.com/problems/number-of-islands/)
- [ ] [Friend Circles](https://leetcode.com/problems/friend-circles/)

### Bitmap

### Bloom-filter

### Bitwise

- [x] [Number of 1 Bits](https://leetcode.com/problems/number-of-1-bits/)
- [x] [Power of Two](https://leetcode.com/problems/power-of-two/)
- [x] [Counting Bits](https://leetcode.com/problems/counting-bits/)
- [ ] [UTF-8 Validation](https://leetcode.com/problems/utf-8-validation/)

### two variable

- [ ] [Maximum Subarray](https://lintcode.com/problem/maximum-subarray/)
- [ ] [Russian Doll Envelopes](https://lintcode.com/problem/russian-doll-envelopes/description)

## System design Problem / Solution sets

### Basic components

#### cache

##### LRU Cache

- [ ] [LRU Cache](https://leetcode.com/problems/lru-cache/)

### Design Twitter (news feed system)

the full system design solution could be found in this blog(Mandarin) [如何设计一个精简版的微博（或者Twitter）？](https://blogs.lirui.me/posts/b637e0c8/)  
and part of the code design problem:

- [ ] [Design Twitter](https://leetcode.com/problems/design-twitter/)

### Design TinyURL

The solution could be found in this blog(Mandarin)[如何设计一个短网址服务](https://blogs.lirui.me/posts/63f58b56/)
and part of the code design problem:

#### Encode and Decode TinyURL

- [ ] [Encode and Decode TinyURL](https://leetcode.com/problems/encode-and-decode-tinyurl/)

## Coding Convention

### Project structure

#### Main parts

* Source sub-project (src)

under the source project the package is named by data structure categories
(such as linkedList, Stack, Queue, BinarySearchTree, PriorityQueue ...)

> Why use "Arrays" instead of "Array"(also string -> strings)?  
> Oops, if named as Array in pyCharm IDE, they can not find the test case module under array package.
> But it works under cli

* Unittest sub-project (tests)

the package naming is exactly ***same*** as the source project

### naming

#### module file naming

##### source project module file

<problem_set_from>_<category>_solution.py 
For example:

leetcode_arrays_solution.py

this module file name means:

1. problem set from "[leetcode](https://leetcode.com/problemset/)"
2. these problems are "arrays" type

> If the problem set from nowhere, this part could be left blank.

##### unittest project module file

Same as the source project, add the prefix "test":

test_<problem_set_from>_<category>_solution.py

### Class naming

Following the [Google style guide (Python) - file naming](http://google.github.io/styleguide/pyguide.html#3163-file-naming)
