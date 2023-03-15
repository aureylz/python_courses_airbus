from random import randint, random, shuffle
from collections import Counter

from unidecode import unidecode

from genetic_utils import GAChallengeBase, GACitizenBase


class ScrabbleDictionary:
    __instance = None

    def __init__(self, rack_letters: list):
        """Virtually private constructor."""
        if ScrabbleDictionary.__instance is not None:
            raise Exception(
                "This class is a singleton! Use the static get_instance() method"
            )
        else:
            ScrabbleDictionary.__instance = self
            self._optimized_dict = dict()
            with open("fr_dictionary.csv") as fr_dict:
                for word in fr_dict.readlines():
                    if len(word) <= 7:
                        sanitized_word = unidecode(
                            word.replace("\n", "").replace(".", "")
                        ).upper()
                        word_len = len(sanitized_word)
                        word_letters_counter = Counter(sanitized_word)
                        rack_letters_counter = Counter(rack_letters)
                        missing_letters_counter = Counter(sanitized_word)
                        missing_letters_counter.subtract(rack_letters_counter)
                        missing_letters = [
                            l for l in missing_letters_counter.elements()
                        ]
                        diff_total = len(missing_letters)
                        if diff_total == 0:
                            if word_len not in self._optimized_dict.keys():
                                self._optimized_dict[word_len] = set()
                            self._optimized_dict[word_len].add(sanitized_word)

    @staticmethod
    def get_instance(rack_letters: list):
        if ScrabbleDictionary.__instance is None:
            ScrabbleDictionary(rack_letters)
        return ScrabbleDictionary.__instance

    def word_exists(self, word: str) -> str:
        sanitized_letters = [l for l in word if not isinstance(l, int)]
        sanitized_word = "".join(sanitized_letters)
        word_size = len(sanitized_word)
        if word_size in self._optimized_dict.keys():
            if sanitized_word in self._optimized_dict[word_size]:
                return sanitized_word
            else:
                return ""
        else:
            return ""

    # def can_make_word_with_letters(self, rack_letters: list):
    #     word = ''.join(rack_letters)
    #     if self.word_exists(word):
    #         return word
    #     else:
    #         if len(rack_letters) >= 2:
    #             for l in rack_letters:
    #                 reduced_rack = rack_letters.copy()
    #                 reduced_rack.remove(l)
    #                 self.can_make_word_with_letters(reduced_rack)
    #         elif len(rack_letters) == 1:
    #             return rack_letters if self.word_exists(word) else None
    #         else:
    #             return None


class SmartScrabbleDictionary:
    def __init__(self):
        self._optimized_dict = dict()
        with open("fr_dictionary.csv") as fr_dict:
            for word in fr_dict.readlines():
                if len(word) <= 7:
                    sanitized_word = unidecode(
                        word.replace("\n", "").replace(".", "")
                    ).upper()
                    word_len = len(sanitized_word)
                    if word_len not in self._optimized_dict.keys():
                        self._optimized_dict[word_len] = {}
                    sorted_letters = "".join(sorted(sanitized_word))
                    if sorted_letters not in self._optimized_dict[word_len].keys():
                        self._optimized_dict[word_len][sorted_letters] = set()
                    self._optimized_dict[word_len][sorted_letters].add(sanitized_word)

    def valid_words_with_letters(self, letters_rack: list):
        for word_size in range(7, 0, -1):
            if word_size != 7:
                letters_rack.pop()
            sorted_rack = "".join(sorted(letters_rack))
            print(word_size, sorted_rack)
            if sorted_rack in self._optimized_dict[word_size].keys():
                return self._optimized_dict[word_size][sorted_rack]


class RackOfLetters(GACitizenBase):
    def __init__(self, genome: list, is_exact_copy: bool = False):
        if is_exact_copy:
            super(RackOfLetters, self).__init__(genome=genome)
        else:
            # create a new genome based on the one passed in,
            # but randomize the letters order
            super(RackOfLetters, self).__init__(genome=None, genome_size=7)
            shuffle(genome)
            self._dna: list = genome

    def mutate(self, mutation_rate: float) -> None:
        before = f"{self}"
        has_muted = False
        for i in range(len(self._dna)):
            if random() < mutation_rate:
                has_muted = True
                swap_with_idx = randint(0, len(self._dna) - 1)
                if swap_with_idx != i:
                    if isinstance(self._dna[i], int):
                        buffer = chr(-self._dna[i])
                        print(
                            f"\t\tmuting {before}: space at position {i} returned to letter {buffer}"
                        )
                    else:
                        buffer = self._dna[i]
                        print(
                            f"\t\tmuting {before}: swapping letters {self._dna[i]} at position {i} and {self._dna[swap_with_idx]} at position {swap_with_idx}"
                        )
                    self._dna[i] = self._dna[swap_with_idx]
                    if isinstance(self._dna[swap_with_idx], int):
                        buffer = chr(-self._dna[swap_with_idx])
                        print(
                            f"\t\tmuting {before}: space at position {i} returned to letter {buffer}"
                        )
                    else:
                        self._dna[i] = self._dna[swap_with_idx]
                        print(
                            f"\t\tmuting {before}: swapping letters {self._dna[swap_with_idx]} at position {swap_with_idx} and {buffer} at position {i}"
                        )
                    self._dna[swap_with_idx] = buffer

                else:
                    if isinstance(self._dna[i], str):
                        self._dna[i] = -ord(self._dna[i])
                        print(f"\t\tmuting {before}: letter {i} becomes a space")
                    else:
                        self._dna[i] = chr(-self._dna[i])
                        print(
                            f"\t\tmuting {before}: space at position {i} returned to letter {self._dna[i]}"
                        )
        if has_muted:
            print(f"\t\t{before} has muted into {self}")

    def reproduce_with(
        self, other_parent: "RackOfLetters", crossover_rate: float
    ) -> tuple["RackOfLetters", "RackOfLetters"]:
        child_1 = RackOfLetters(genome=self._dna.copy())
        child_2 = RackOfLetters(genome=other_parent._dna.copy())
        if random() < crossover_rate and len(self._dna) > 2:
            pt = randint(1, len(self._dna) - 2)
            child_1_start_dna = self._dna[:pt]
            child_1_end_dna = self._dna[pt:]
            shuffle(child_1_end_dna)
            child_1_dna = child_1_start_dna + child_1_end_dna
            child_1 = RackOfLetters(genome=child_1_dna, is_exact_copy=True)
            child_2_start_dna = other_parent._dna[:pt]
            child_2_end_dna = other_parent._dna[pt:]
            shuffle(child_2_end_dna)
            child_2_dna = child_2_start_dna + child_2_end_dna
            child_2 = RackOfLetters(genome=child_2_dna, is_exact_copy=True)
            print(
                f"\tbreed({self} x {other_parent}, cross_over_position={pt} => ({child_1}, {child_2})"
            )
        else:
            print(
                f"\tbreed({self} x {other_parent}, no_cross_over => ({child_1}, {child_2})"
            )
        return child_1, child_2

    @property
    def fitness(self) -> float:
        fr_dict = ScrabbleDictionary.get_instance(self._dna)
        word = fr_dict.word_exists(self._dna)
        if word:
            return len(word)
        else:
            return 0

    def __str__(self):
        """
        str() is used for creating output for end user.str’s goal is to be readable.
        :return:
        """
        dna = "".join(
            str(letter) for letter in self._dna if not isinstance(letter, int)
        )
        return f"{dna} ({self.fitness})"

    def __repr__(self):
        """
        repr() is mainly used for debugging and development.repr’s goal is to be unambiguous.
        """
        dna = "".join(
            str(letter) for letter in self._dna if not isinstance(letter, int)
        )
        return f"RackOfLetters({dna})"


class ScrabbleChallenge(GAChallengeBase):
    def __init__(self, initial_rack: str = None, population_count: int = 500):
        genome_size = 7
        super().__init__(
            population_count=population_count,
            genome_size=genome_size,
            fitness_threshold=genome_size,
            max_generations=50,
            crossover_rate=0.5,
            mutation_rate=0.1,
        )
        if not initial_rack:
            initial_rack = []
            for i in range(genome_size):
                initial_rack.append(chr(ord("A") + randint(0, 25)))
        self._pop = [
            RackOfLetters(genome=[l for l in initial_rack])
            for _ in range(population_count)
        ]
        print(f"Available letters: {initial_rack}")
