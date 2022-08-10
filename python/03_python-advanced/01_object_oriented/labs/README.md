# Oriented Object Hands-On

In this lab, we'll be leveraging OOP to implement a versatile [Genetic Algorithm](https://en.wikipedia.org/wiki/Genetic_algorithm) that can be used to soleve differents problems.

As per Wikipedia:

> G-A are inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). 
>
> Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on biologically inspired operators such as mutation, crossover and selection

This is a non-deterministic way to find acceptable solutions in a minimum amount of time for complex problems.

For that to work, the problem you're trying to solve must be modelizable with chromosoms and there must be a way to evaluate a given chromosom to 'measure' how far it is from the optimal solution.

## Available material

Because the whole purpose of this lab is to manipulate classes and objects and not focusing on algorithm implementation, we are providing you with some existing code:

- [genetic_utils.py](genetic_utils.py) implements the mutation, crossover and selection operators; it also contains a full implementation of the genetic algorithm that uses those operators.
- [main.py](main.py) uses the above tools to find a solution to the OneMax problem.

All this code is working but is implemented in the form of functions and doesn't use the power of the OOP.

We want to make it more generic, so that, the same code can be used to solve different kind of problems with just implementing a new class that models the problem to solve.

### Fitness function

It tells how good is a given citizen when it comes to a specific problem resolution.

Here, in the OneMax challenge, the fitness function is just the sum of the ones.

### Genetic operators

It mimics the genetic on natural entities (humans, plants, animals...)

#### Mutation

At random rate, a mutation can occur, a mutation is simply a bit swap in a DNA chain, for instance:

```100101001``` => ```000101001``` (here the first bit changed from 1 to 0)

#### Cross-Over

This models a basic reproduction process in which 2 parents will generate 2 childs.
The childs DNA chain will be composed of some of the DNA from parent 1 and some DNA from parent 2:

To achieve this, the cross-over operator will choose a random position in the DNA chain, everything before this index will be taken from parent 1 and the rest from parent 2:

Example:

Let say our split index will be 3, which means, we'll be taking the first 3 chromosoms from parent 1 and the rest from parent 2.

```11111111```: Parent 1 DNA

```00000000```: Parent 2 DNA

```___|____```: Split index / position

```11100000```: Child DNA

#### Selection

Is a kind of tournament to decide which citizen in the population will become reproducers.
The idea is to flavor the citizen who are the more adaptated to their environment (have the best fitness function).

#### The G-A algo

Will put all the above concepts together (genetic operators, fitness....) on a random population and will compute several new generations to try to converge on one acceptable solution.

## The One Max problem

In the OneMax challenge, the goal is to get maximize the amount of 1 in a list of boolen values.

The list of O and 1 will form the DNA of one citizen in our population.

For instance, if we consider a 8 bits genoma:

```100101001``` is one possible DNA chain, ```110100101``` is another one.

```11111111``` contains 8 times the digit ```1``` and is the best solution we can find with an 8 bits length DNA chain.

### Sample runs

Here we're using a 32 bits size genome.
Mutiple runs will lead to different ways of browsing the entire search space.
The random nature of mutations and cross-over is what brings diversity.
The selection operator helps converging to an acceptable solution.
Some parameters can be changed to influence the internal behavior like mutation or cross-over rate, the amount of citizens in the population, the size of the genome...

#### Run #1

```
Generation #:0
	Found a better candidate citizen (fitness=  18 and DNA=10101001100011011101100100111110)
	Found a better candidate citizen (fitness=  19 and DNA=00111011100101011111110001010011)
	Found a better candidate citizen (fitness=  20 and DNA=11010100010110111001111101110110)
	Found a better candidate citizen (fitness=  21 and DNA=10010110001111111001111101110101)
	Found a better candidate citizen (fitness=  22 and DNA=10110111111101101001011110110011)
Generation #:1
	Found a better candidate citizen (fitness=  23 and DNA=01110110001111111001111101110111)
	Found a better candidate citizen (fitness=  24 and DNA=11111111100111011010001101111111)
Generation #:2
	Found a better candidate citizen (fitness=  25 and DNA=11111111110111011010101110111011)
Generation #:3
	Found a better candidate citizen (fitness=  26 and DNA=11101111110111111011001111111110)
	Found a better candidate citizen (fitness=  27 and DNA=11111111110111111011001111111110)
Generation #:4
	Found a better candidate citizen (fitness=  29 and DNA=11111111011110111111111101111111)
Generation #:5
	Found a better candidate citizen (fitness=  30 and DNA=11111111111110111111111101111111)
Generation #:6
	Found a better candidate citizen (fitness=  31 and DNA=11111111111111111110111111111111)
Generation #:7
Generation #:8
Generation #:9
	Found a better candidate citizen (fitness=  32 and DNA=11111111111111111111111111111111)
I guess I found an acceptable solution (algorithm converged in 9 generations)
Done!
Fitness 32 => DNA=11111111111111111111111111111111
```

#### Run #2

```
Generation #:0
	Found a better candidate citizen (fitness=  18 and DNA=11111101000101011111000100001011)
	Found a better candidate citizen (fitness=  19 and DNA=10011100111100010111001110001111)
	Found a better candidate citizen (fitness=  22 and DNA=11011110100100111101011011101111)
	Found a better candidate citizen (fitness=  23 and DNA=10011110001011111110111111110011)
Generation #:1
	Found a better candidate citizen (fitness=  27 and DNA=11111101111011111110111111110011)
Generation #:2
Generation #:3
	Found a better candidate citizen (fitness=  28 and DNA=11111101111101111111111101101111)
Generation #:4
Generation #:5
	Found a better candidate citizen (fitness=  29 and DNA=11111111111101110111111101111111)
Generation #:6
Generation #:7
Generation #:8
	Found a better candidate citizen (fitness=  30 and DNA=11111101111011111111111111111111)
	Found a better candidate citizen (fitness=  31 and DNA=11111101111111111111111111111111)
Generation #:9
Generation #:10
	Found a better candidate citizen (fitness=  32 and DNA=11111111111111111111111111111111)
I guess I found an acceptable solution (algorithm converged in 10 generations)
Done!
Fitness 32 => DNA=11111111111111111111111111111111
```