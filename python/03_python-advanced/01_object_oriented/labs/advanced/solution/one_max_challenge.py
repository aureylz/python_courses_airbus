from random import randint, random, getrandbits

from genetic_utils import GAChallengeBase, GACitizenBase


class OneMaxCitizen(GACitizenBase):
    def __init__(self, genome_size: int, genome: list = None):
        super(OneMaxCitizen, self).__init__(genome=genome, genome_size=genome_size)
        if not genome:
            dna = getrandbits(genome_size)
            dna_str: str = format(dna, f'0{genome_size}b')
            self._dna = [1 if gene == "1" else 0 for gene in dna_str]

    def mutate(self, mutation_rate: float) -> None:
        before = f'{self}'
        has_muted = False
        for i in range(len(self._dna)):
            if random() < mutation_rate:
                self._dna[i] = 1 - self._dna[i]
                has_muted = True
                # print(f'\t\tflipping bit {i}', end='')
        # if has_muted:
        #    print(f'\t\t{before} has muted into {self}')

    def reproduce_with(self,
                       other_parent: 'OneMaxCitizen',
                       crossover_rate: float) -> tuple['OneMaxCitizen', 'OneMaxCitizen']:
        child_1 = OneMaxCitizen(genome=self._dna.copy(), genome_size=self._genome_size)
        child_2 = OneMaxCitizen(genome=other_parent._dna.copy(), genome_size=self._genome_size)
        if random() < crossover_rate:
            pt = randint(1, len(self._dna) - 2)
            child_1 = OneMaxCitizen(genome=self._dna[:pt] + other_parent._dna[pt:], genome_size=self._genome_size)
            child_2 = OneMaxCitizen(genome=other_parent._dna[:pt] + self._dna[pt:], genome_size=self._genome_size)
            print(f'\tbreed({self} x {other_parent}, cross_over_position={pt} => ({child_1}, {child_2})')
        else:
            print(f'\tbreed({self} x {other_parent}, no_cross_over => ({child_1}, {child_2})')
        return child_1, child_2

    @property
    def fitness(self) -> float:
        return sum(self._dna)

    def __str__(self):
        """
        str() is used for creating output for end user.str’s goal is to be readable.
        :return:
        """
        dna = ''.join(str(gene) for gene in self._dna)
        return f'{dna} ({self.fitness})'

    def __repr__(self):
        """
        repr() is mainly used for debugging and development.repr’s goal is to be unambiguous.
        """
        dna = ''.join(str(gene) for gene in self._dna)
        return f'OneMaxCitizen({dna})'


class OneMaxChallenge(GAChallengeBase):
    def __init__(self, population_count: int, genome_size: int):
        super().__init__(population_count=population_count,
                         genome_size=genome_size,
                         fitness_threshold=genome_size,
                         max_generations=300,
                         crossover_rate=0.9,
                         mutation_rate=1.0 / float(genome_size))
        self._pop = [OneMaxCitizen(genome=None, genome_size=genome_size) for _ in range(population_count)]