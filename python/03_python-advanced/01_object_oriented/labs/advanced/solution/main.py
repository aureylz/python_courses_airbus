from one_max_challenge import OneMaxChallenge
from scrabble import ScrabbleChallenge, ScrabbleDictionary


def main():
    # one_max_challenge = OneMaxChallenge(population_count=100, genome_size=64)
    # one_max_result = one_max_challenge.solve_challenge()
    # print('OneMax challenge done!')
    # print(one_max_result)
    # print(ScrabbleDictionary().get_instance().valid_words_with_letters(['A', 'V', 'E', 'C', 'X', 'Y', 'Z']))
    # scrabble_challenge = ScrabbleChallenge()
    scrabble_challenge = ScrabbleChallenge(initial_rack="ABEILLE")
    scrabble_result = scrabble_challenge.solve_challenge()
    print("Scrabble challenge done!")
    print(scrabble_result)


if __name__ == "__main__":
    print("Python Basics Labs Solution : OOP Genetic algorithm")
    main()
