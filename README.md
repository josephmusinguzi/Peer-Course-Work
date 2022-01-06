# Peer to peer Course work
Demonstration of Peer to peer

introduction

Peer to peer network allows computers to communicate directly without a need for centralized servers. A peer uploads or downloads directly from it’s peers instead of accessing it form the joint server.
This document shows the implementation of a peer to peer program to show file sharing in peer to peer architecture.

implementation.



The project is written in python. It comprises of 4 files, The server, Peer1, Peer2 and ContentDisplay.

The server is to create a socket and act as a file manager for all peers connecting in the peer peer architecture.

The Peer1, being the first peer initiated, it defines which files it has for sharing and addresses the location for the files to be accessed by the other peers.

The Peer2, acting as second peer in the connection, it acts as a peer requesting for file from any other peers and downloads the files and can equally share contents with other peers.

The ContentDisplay is responsible for listening to peers for new files added and can be accessed by all peers to show location of files and files themselves.




implementation-Action.

To Run the project, follow the steps below.
    1. Run the ContentDisplay.py
    2. Run Peer1.py.  This is to announce chunks to other peers.
    3. Run Server.py
    4. Run Peer2.py. Then choose which file from the ContentDisplay.py to download.


