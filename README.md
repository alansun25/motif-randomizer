# Network Randomization: Triadic Motif Frequency

This Python script takes an input network and randomizes it by increasing or decreasing 
the frequency of a partiular triadic motif, while preserving degree sequence. Users can
input a network as a text file, select a motif of interest, and specify whether to
increase or decrease the frequency of the motif.

A <ins>**triadic motif**</ins> is a small, connected, 3-node subgraph in which the configuration of the links is predefined (2 possible triadic motifs in undirected networks; 13 possible in directed networks).

# Approach
- Randomly choose 2 links in the network.
- Swap link ends (i.e. originally have a → b and c → d; swap to a → d and c → b).
    - Preserves degree sequence.
- Make sure the swap does not result in self-loops or parallel edges.
- Calculate frequency of specified motif in neighborhood before and after each swap.
    - “Neighborhood” defined as set of all in- and out-neighbors of the four nodes belonging to the two swapped edges.
- Decide whether to keep or discard link swap based on change in frequency and user-specified behavior.

