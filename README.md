# Battleship Application

>This implementation will be based on a symmetric client server architecture, where each player has both a server and a client. The server keeps an internal state of the game and issues replies to the other player’s client.
---

# Board Description

- Carrier(C) = 5
- Battleship(B) = 4
- Cruiser(R) = 3
- Submarine(S) = 3
- Destroyer(D) = 2
- (_) = Water

---

# Messages

The ‘fire’ message will be represented as an HTTP POST request. The content of the fire message will include the targeted coordinates as a URL formatted string for Web forms, for example 5 and 7, as: x=5&y=7. Assume that coordinates are 0-indexed.
The ‘result’ message will be formatted as an HTTP response. For a correctly formatted ‘fire’ request your reply will be an HTTP OK message with hit= followed by 1 (hit), or 0 (miss). If the hit results in a sink,
then the response will also include sink= followed by a letter code (C, B, R, S, D) of the sunk ship. An example of such a reply is hit=1&sink=D.
If the fire message includes coordinates that are out of bounds, the response will be HTTP Not Found. If the fire message includes coordinates that have been already fired opon, the response will be HTTP Gone. Finally, if the fire message is not formatted correctly, the response will be HTTP Bad Request.
