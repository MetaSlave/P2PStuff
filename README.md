# P2PStuff
My attempt at creating a mini P2P network file sharing thing over the internet without router configurations


The Concept
- Peers are nodes in a network
- Distributed Hash Table looks up and stores files
- Use NAT Traversal Techniques to allow for file sharing over 2 different NATs

DHT (CHORD)
- N nodes in network ordered in a circle
- Hash used to assign Node ID and resources
- Hash of Node IP = ID
- Hash of File Name = Key
- Hashspace = number of files and nodes
- Resource of key is stored at Node where ID = Key,else stored at next highest ID
- Nodes are ordered by ID
- When Node leaves or joins network, keys must be reassigned to successor
- Each Node maintains a routing table with nodes 1, 2, 4, 8 positions away
e.g. For 16 nodes using a 4 bit hash algo,

Hash of file = 4 bit output (001) or (3)
This file needs to be stored on Node 3.
If Node 3 does not exist, try Node 4 and 5 and 6 and so on.
For 4 bit hash value, there is 4 to the power of 2 possible number of files and nodes

To insert data,
- Hash file name data to get key
- Routing is used to find node that stores key, ID = key
- Data is stored on node

To search for data,
- Hash file name data to get key
- Routing is used to find node that stores key, ID = key
- Retrieve data from found node

Advantages of CHORD
- When finding successor node, complexity is low as only 1, 2, 4, 8 nodes are affected
- Thus leaving and joining nodes have very little complexity


NAT Traversal (UDP Hole Punching)
- Node 1 and Node 2 send UDP Packets to Boostrap Node
- NAT in both Node 1 and 2 creates entry which maps IP of nodes to IP of RS



























Resources (DHT):
https://www.youtube.com/watch?v=qqv4OJ5Lc4E
https://en.wikipedia.org/wiki/Chord_(peer-to-peer)
https://en.wikipedia.org/wiki/Pastry_(DHT)
https://medium.com/karachain/peer-to-peer-protocols-explained-3b1d947c4600 

Resources (NAT Traversal):
https://samy.pl/chownat/
https://www.quora.com/Is-a-pure-P2P-network-possible-and-does-one-exist
https://www.youtube.com/watch?v=nHwt21D9ZaE
https://stackoverflow.com/questions/51004291/how-to-communicate-between-two-nodes-behind-nat