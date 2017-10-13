Trip Planning Under Uncertainty
===============================

This repository contains all code used to compare the Dijkstra and MCTS algorithm for planning under uncertainty.

* The code can be thought of as separated into four different parts *

** Construction of the graph **

See the files builder.py, graph.py and update_map.sh

These are used to construct the graph that we used for testing.

The "Game"
----------

See the files map.py and traveller.py

In these files we digest the information produced by the Builder and apply all logic, such as connections, variance, delays etc. The traveller class is responsible for making sure no invalid or unresonable moves can be made.

The Dijkstra implementation
---------------------------

See Dijkstra.py

Here the Dijkstra algorithm is implemented and tested.

The MCTS algorithm
------------------

See mcts/mcts.py and mcts.py

The library is used to define the mcts algorithm generally.
And it is then used for our specific case in the mcts.py file
to test the algorithm.
