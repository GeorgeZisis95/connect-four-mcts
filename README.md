# Implementation of Monte Carlo Tree Search

This project aims to implement Monte Carlo Tree Search for simple combinatorial games like TicTacToe or ConnectFour. 

### Game Information

By testing Monte Carlo Tree Search in the simple game of Connect Two with a board size of 1x4 I reached the conclusion that the simplicity of the game makes it hard for the developer to diagnose potential issues of the implementation.

On the other hand, classic Connect Four with a board size of 6x7 requires a good amount of time for each move to be calculated which leads to big testing times. Additionally, since my own level of play is not good I cannot successfully deduce if the agent's play is good or if it is a blunder. 

This leads me to create a middle ground game called Connect Three with a board of 4x4. I can easily deduce when the agent makes a blunder and it only takes a few seconds for the agent to make a move of high enough depth.

## Results

### Connect Three

The first step is creating the game environment. My first approach was to create a class Attribute for both the game board and the current player. With this approach keeping track of the correct board and player proved to be extremely hard since Monte Carlo Tree Search requires a lot of back and forth throughout each simulation.

The alternative is much simpler. Inside the game class I create methods that return the valid actions, the state or the winner of the game given the board and the player as parameters. This gives the developer much more control and is much easier to debug than the previous approach.

As for the Tree Search itself, I created a separate Node class which keeps track of each node's board state, the correct player's turn and parent node. It also stores each node's visitation count and value as well as the uct method needed in the selection phase. Last but not least, the Node.expand() method selects an unexplored action from the current node, uses it to create a child node which then is stored to the current node's explored children and is returned for use in the Tree Search.

The Tree Search class implements the selection, rollout and backpropagation stage.
 - During the selection the agent searches for a leaf node by checking if the current node is not fully expanded. If it is fully expanded it moves to the node with the highest uct score. I found a good exploratory constant(c_puct) for Connect Three to be 2. When a leaf node is reached it is expanded.

 - After the selection phase the node is passed in the rollout stage. Important here is to check for a terminal node right at the start since a terminal node can be returned from the selection phase. After this, a random game is created and the method returns the reward. A simple mistake that is easily made is to update the player before checking for termination which leads to wrong results.

 - The backpropagation phase is recursively updating each node's visit count and total value until the root node is reached. If the player of the node and the result of the game are the same the node's value is incremented by 1 else it is decreased by 1.

 The only two hyperparameters are the number of simulations and the c constant for the uct formula. I observe that 10000 simulations are more than enough for Connect Three and I've set the c constant to 2 even though the general consensus is 1.41 because I observed better performance. 

### Connect Four

I didn't have to change anything in my implementation for the agent to play Connect Four. I tested it with the same c constant and a total of 10000 simulations and it plays out at a decent level. It keeps choosing the middle column as its first move which is a great sign, since it is mathematically proven to be the best opening in the game. 

## Requirements

There are no special requirements for vanilla Monte Carlo Tree Search. I've built the entire project using just Python and the Numpy Library.

## Future Improvements

- Run simulations in parallel to reduce search time.
- Replace rollout stage with a neural network.
- Create minimax tree search to compare the agents.