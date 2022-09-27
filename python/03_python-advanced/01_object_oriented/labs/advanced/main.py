from random import getrandbits

from genetic_utils import darwin

# The problem is called OneMax and evaluates a binary string based on the number of 1s in the string.
# For example, a bitstring with a length of 20 bits will have a score of 20 for a string of all 1s.


def init_population_onemax(population_count: int, genome_size: int):
    def init_citizen():
        dna = getrandbits(genome_size)
        dna_str: str = format(dna, f'0{genome_size}b')
        # print(f'Creating initial citizen (DNA={dna_str}\t{dna:8})')
        return [1 if gene == "1" else 0 for gene in dna_str]

    return [init_citizen() for _ in range(population_count)]


def fitness_onemax(citizen_dna: list) -> float:
    """counts the amount of bits set to true, (the more the better in the OneMax challenge)"""
    return sum(citizen_dna)


def decode_onemax(citizen_dna: list) -> int:
    """
    returns the decoded dna which was passed-in (in the context of the OneMax challenge)
    :param citizen_dna: the genetic material in the form of an array of genes
    :return: an unsigned integer that represents the citizen for the OneMax challenge 
    """
    return int(''.join([str(gene) for gene in citizen_dna]), 2)


def main():
    # max num of generations if the algo does not converge before
    max_generations = 300
    # quantity of bits in the genome
    genome_size = 32
    # population size
    population_count = 100
    # crossover rate
    crossover_rate = 0.9
    # mutation rate
    mutation_rate = 1.0 / float(genome_size)
    best, score = darwin(
        init_population_fn=init_population_onemax,
        fitness_fn=fitness_onemax,
        fitness_threshold=genome_size,  # the target here is to get a citizen whose DNA is only made of 1 (no 0)
        decode_fn=decode_onemax,
        genome_size=genome_size,
        max_generations=max_generations,
        population_count=population_count,
        crossover_rate=crossover_rate,
        mutation_rate=mutation_rate)
    print('Done!')
    binary_dna = ''.join(str(gene) for gene in best)
    print(f'Fitness {score} => DNA={binary_dna}')


if __name__ == '__main__':
    print('Python Basics Labs : Genetic algorithm')
    # print("""Inspired on August 1rst 2022 by "Jason Brownlee@Machine Learning Mastery"
    #      Source: https://machinelearningmastery.com/simple-genetic-algorithm-from-scratch-in-python/
    #      Copy-left: https://machinelearningmastery.com/faq/single-faq/can-i-use-your-code-in-my-own-project/""")
    main()
