# University of Strathclyde -  MSc Artificial Intelligence and Applications
## CS814 - Artificial Intelligence for Autonomous Systems
## Assignment 1 - MIU
File Created first created 4th October 2019 by Barry Smart.

### Overview
The assignment was to create an algorithm which can for search strings of the MIU system  presented in Chapter 1 of [Gödel, Escher, Bach](https://www.amazon.co.uk/Godel-Escher-Bach-Eternal-Golden/dp/0465026567/).

The MIU system is presented as a puzzle:
> Can you transform the string MI into the string MU?

In order to accomplish this, you are given the following rules:
1. If your string ends with an I character, you can add a U on the end: xI -> xIU
2. If the string starts with an M character, you can double what comes after it: Mx -> Mxx
3. If you have three consequetive I characters, you can replace it with a U: xIIIy -> xUy
4. If you have two consequetive U characters, you can delete them altogeether: xUUy -> xy

This problem is an excellent introcuction to search algorithms.

In the terminology of the book, the starting state "MI" is called the *Axion* and the desired goal state is called the *Theorem*.

Thinking about defining the specific environment in which our AI will be operating:
- The search space is infinite;
- **It turns out that transforming MI into MU is impossible**, but you can derive lots of other strings!

### Approach
We were given some guidance about how to tackle this first assigment:
- Begin with writing a function next_states(s), which given a string s will return all possible strings that can be derived from s (using the rules defined above) in a **single step**;
- Then think about applying a "breadth-first" search approach - write a function search_for(t), that given goal state t will find the shortest path to achieving the goal;

### Breadth First Search
Breadth first search is a simple approach to tackling a *uninformed search* or *blind search*.



### Solution
Description of solution here...

### Environment used to build the solution
See seperate README document **TO DO** that describes my general setup for writing Python.

### How to run it
Point towards notebook to get insight into how to run it...
