# CS 170 Project 1: The Eight Puzzle

## Project Description
This project implements algorithms to solve the 8-puzzle game and then for any general N-puzzles using uniform-cost search and A* search with heuristics.

## Algorithms Implemented
1.  **Uniform Cost Search:** A* search with h(n) = 0.
2.  **A* with Misplaced Tile Heuristic:** Counts the number of tiles not in their goal position.
3.  **A* with Manhattan Distance Heuristic:** Sum of the vertical and horizontal distances of each tile from its goal position.

## Files
* `main.py`: Contains the main code, search algorithms, and heuristic functions.

## Usage
Run program using:
`python main.py`

After running, follow the on-screen prompts to select a default puzzle or enter a custom puzzle.

## Performance Comparison
For the example puzzle `[[1, 2, 3], [4, 8, 0], [7, 6, 5]]`:
- **Uniform Cost Search**: 35 nodes expanded
- **A* with Misplaced Tile**: 8 nodes expanded
- **A* with Manhattan Distance**: 5 nodes expanded

The heuristics significantly reduce the search space.

## Citations
* **Project Prompt and Pseudocode**: Dr. Eamonn Keogh, CS 170 Slides ( "3__Heuristic Search"), 2026.
* **Python Documentation**: https://docs.python.org/3/ (for `heapq` and `copy` modules).

## Status
* [x] Initial Repository Setup
* [x] Main Driver Skeleton (matches the pseudocode)
* [x] Implementation of Node class and State representation
* [x] Implementation of EXPAND function (operators)
* [x] Implementation of Search Algorithms (UCS, A*)
* [x] Implementation of Heuristics (Misplaced Tile, Manhattan Distance)
* [x] Testing and Report 