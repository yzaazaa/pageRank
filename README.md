# PageRank Algorithm

Welcome to the **PageRank** project! This repository contains an implementation of the PageRank algorithm, a technique widely used to rank webpages based on their importance. The algorithm simulates a "random surfer" navigating through the web using both **Monte Carlo** methods for efficient approximation and **Markov Chains** for iterative updates, offering flexibility in how ranks are computed.

## Features

- **Random Surfer Model**: Simulates the behavior of a web surfer by modeling the probability of visiting different pages based on links between them.
- **Monte Carlo Simulation**: Uses random sampling techniques to efficiently estimate PageRank values, reducing computational overhead while providing accurate approximations.
- **Markov Chains**: Implements the PageRank process as a Markov Chain, iteratively updating the rank values based on the structure of the graph until convergence.
- **Configurable Parameters**: Easily adjust parameters like damping factor, number of samples, and iteration limits to suit different use cases.


## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Algorithm](#algorithm)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yzaazaa/pageRank.git
   ```
2. Navigate to the project directory:
   ```bash
   cd pageRank
   ```
3. Ensure you have Python installed (version 3.7 or above).

## Usage

Run the main script to compute PageRank:

```bash
python pagerank.py [corpus]
```

## Examples

```
PageRank Results from Sampling (n = 10000)
  bfs.html: 0.1132
  dfs.html: 0.0798
  games.html: 0.2319
  minesweeper.html: 0.1173
  minimax.html: 0.1294
  search.html: 0.2063
  tictactoe.html: 0.1221
PageRank Results from Iteration
  bfs.html: 0.1143
  dfs.html: 0.0802
  games.html: 0.2287
  minesweeper.html: 0.1186
  minimax.html: 0.1310
  search.html: 0.2083
  tictactoe.html: 0.1189
```

## Algorithm

The PageRank algorithm ranks webpages based on their importance by simulating a "random surfer" navigating through the web. The process can be implemented in two distinct ways: **Monte Carlo Simulation** and **Markov Chain Iteration**.

## Monte Carlo Method

The **Monte Carlo method** used in this implementation approximates the PageRank values by simulating the random surfer model through random walks. In this method, the surfer's path is determined by randomly selecting pages according to a probabilistic model that reflects the structure of the web. By repeating this random walk many times (`n` samples), we can estimate the probability of visiting each page. This is a faster way to approximate PageRank for very large datasets when exact calculation through iteration would be too expensive.

Key features of this method:
- Efficient for large graphs with many pages.
- Uses random sampling to estimate the distribution of the surfer's visits across pages.
- Results in a faster but approximate solution to the PageRank values.

## Markov Chain Method

The **Markov Chain method** calculates the PageRank by modeling the web as a Markov process, where the state of the random surfer is updated based on transition probabilities between pages. The process involves iteratively updating the PageRank values by considering how much rank a page receives from other pages that link to it. This method uses the structure of the graph to compute the rank values, and it converges to the true PageRank values as the algorithm runs.

Key features of this method:
- Computes exact PageRank values.
- Converges to a stable set of rank values after a number of iterations.
- Suitable for smaller graphs or when higher accuracy is required.

---

Feel free to explore the code, experiment with different datasets, and share your feedback!