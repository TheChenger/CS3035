# CS3035
Programming Language Paradigms

Drunkard's Walk:

This program takes in *n* as the number of intersections traversed over a grid of streets that our drunkard stumbles through, they start at (0,0). The user is asked how many intersections the person goes through and after gives the coordinates of the person.


The Game of Nim:

The game of Nim is played as follows.  Two players alternately take marbles from a pile. In each move, a player chooses how many marbles to take. The player must take at least one but at most half of the marbles. Then the other player takes a turn. The player who takes the last marble loses. In this program the user is pitted against a CPU.

- We generate a random integer between 10-100 to start the size of the pile.
- We generate a random integer between 0-1 to decide whether the computer or human takes the first turn
- We generate a random integer between 0-1 to decide whether the computer plays smart or stupid

In stupid mode the computer simply takes a random legal value (between 1 and n/2) from the pile whenever it has a turn.

In smart mode the computer takes off enough marbles to make the size of the pile a power of two minus 1, that is, 3, 7, 15, 31, or 63. This is always a legal move, except when the size of the pile is currently one less than a power of two. In that case, the computer makes a random legal move.

The computer cannot be beaten in smart mode when it has the first move, unless the pile size happens to be 15, 31, or 63. Of course, a human player who has the first turn and knows the winning strategy can win against the computer.


Perfect Numbers:

A positive integer is called a perfect number if it is equal to the sum of all of its positive divisors, excluding itself. For example, 6 is the first perfect number because 6 = 3 + 2 + 1. The next is 28 = 14 + 7 + 4 + 2 + 1.  The program asks the user for a value *n* and displays all perfect numbers from 6 to n.  ***NOTE: There are not many perfect numbers so you may only have a few results depending on the input value.***
