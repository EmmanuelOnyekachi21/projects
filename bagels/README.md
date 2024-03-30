This is a deductive logic game.  You must guess a secret three digit number based on clues.  The game offers one of the following hints in response to your guess:
```python
"Pico": when your guess has a correct digit in the wrong place.
"Fermi": when your guess has a correct digit in the correct place.
"Bagels": when your guess has no correct digit(s).
```

You have 10tries to guess the secret number.

### Getting started 

1. Ensure you're using the latest python version (python 3.x.).
You could confirm using:
```python
python --version
```
2. Clone this repository:
```python
        git clone https://github.com/EmmanuelOnyekachi21/bagels.git
```
3. Run the game script using Python:
```python
    python3 bagels.py
```
### The Program in Action

When you run: 
```python
bagels.py
```
the output would look like this:
```python
Bagels, a deductive logic game.
By Emmanuel Nnabugwu

I am thinking of a 3-digit number. Try to guess what it is.
Here are some clues:
When I say: That means:
Pico One digit is correct but in the wrong position.
Fermi One digit is correct and in the right position.
Bagels No digit is correct.
I have thought up a number.
You have 10 guesses to get it.
Guess #1:
> 123
Pico
Guess #2:
> 456
Bagels
Guess #3:
> 178
Pico Pico
--snip--
Guess #7:
> 791
Fermi Fermi
Guess #8:
> 701
You got it!
Do you want to play again? (yes or no)
> no
Thanks for playing!
``` 
