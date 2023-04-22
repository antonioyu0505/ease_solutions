# Longest Descending Path in a Matrix

This script reads a matrix of integers from standard input and computes the longest descending path in it. A path is considered descending if it only goes through cells with strictly decreasing values, and its drop is the difference between the first and last cells of the path.

# Requirements

Python 3.6 or higher

# Running the Program
The program expects the first line of input to contain two integers, n and m, separated by a space, representing the dimensions of the matrix. The following n lines contain m integers each, representing the elements of the matrix.

To run the program, simply run the script and input the matrix as described above:

```console
$ python longest_descending_path.py < 4x4.txt
Length of calculated path: 5
Drop of calculated path: 8
Calculated path: 9-5-3-2-1
```
The program will output the length of the longest descending path, the drop of the path, and the path itself.


# Approach
The program uses a depth-first search (DFS) algorithm to traverse the matrix and find all possible paths of decreasing integers. Starting from each cell in the matrix, the program recursively explores all adjacent cells that contain a smaller integer than the current cell. The program keeps track of the longest path found and returns it at the end.

In order to break ties between paths of the same length, the program uses the difference between the largest and smallest values in the path as a tiebreaker.

The program implements memoization by marking visited cells to avoid exploring the same cell twice.