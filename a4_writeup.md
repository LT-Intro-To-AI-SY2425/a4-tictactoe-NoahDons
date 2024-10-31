# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
Getting to understan how object oriented programming works in python. I have sme experience with lua and java so it wasn't as bad trying to understand oop in pythob as it could have been, but it was still a little akward.

2. Explain how you would add a computer player to the game.
I would create an object that represents the computer. The object would have several methods that it would call to help decide what move to make.

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.

I would have the computer scan the board for any winning moves that the AI could make then see if the player could make any winning moves and block them. I would then look for a move that neighbors both an empty space and another one of the computer's tiles making sure it makes a line. If all else fails it would play a random move.