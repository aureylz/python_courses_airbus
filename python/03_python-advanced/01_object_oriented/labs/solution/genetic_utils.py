from abc import ABC, abstractmethod
from random import randint
from collections import namedtuple
from sys import float_info

GAChallengeResult = namedtuple('GAChallengeResult', 'citizen_dna fitness_value')


class GACitizenBase(ABC):

    def __init__(self, genome: list = None, genome_size: int = None):
        super(GACitizenBase, self).__init__()
        if not genome:
            self._dna: list = []
            self._genome_size: int = genome_size
        else:
            self._dna: list = genome
            self._genome_size: int = len(genome)
        # print(f'new {type(self).__name__}({self})')

    @abstractmethod
    def mutate(self, mutation_rate: float) -> None:
        ...

    @abstractmethod
    def reproduce_with(self, other_parent: 'GACitizenBase', crossover_rate: float) -> tuple['GACitizenBase', 'GACitizenBase']:
        ...

    @property
    @abstractmethod
    def fitness(self) -> float:
        ...


class GAChallengeBase(ABC):
    def __init__(self,
                 fitness_threshold: float,
                 population_count: int = 150,
                 genome_size: int = 16,
                 max_generations: int = 100,
                 crossover_rate: float = 0.9,
                 mutation_rate: float = 0.05):
        super(GAChallengeBase, self).__init__()
        self._fitness_threshold: float = fitness_threshold
        self._population_count: int = population_count
        self._genome_size: int = genome_size
        self._max_generations: int = max_generations
        self._crossover_rate: float = crossover_rate
        self._mutation_rate: float = mutation_rate
        self._pop: list[GACitizenBase] = []
        print(f"""{type(self).__name__}(
                {self._fitness_threshold=}, 
                {self._population_count=}, 
                {self._genome_size=}, 
                {self._max_generations=}, 
                {self._crossover_rate=}, 
                {self._mutation_rate=})""")

    @staticmethod
    def _choose_breeder(pop: list, scores: list, k: int = 3):
        selection_ix = randint(0, len(pop) - 1)
        for _ in range(k):
            ix = randint(0, len(pop) - 1)
            if scores[ix] > scores[selection_ix]:
                selection_ix = ix
        return pop[selection_ix]

    def _create_next_generation(self, breeders: list[GACitizenBase]):
        new_children: list = []
        for j in range(0, len(breeders) - 1, 2):
            citizen_1, citizen_2 = breeders[j], breeders[j + 1]
            child_1, child_2 = citizen_1.reproduce_with(citizen_2, crossover_rate=self._crossover_rate)
            for c in (child_1, child_2):
                c.mutate(mutation_rate=self._mutation_rate)
                new_children.append(c)
        # print(new_children)
        return new_children

    def solve_challenge(self) -> GAChallengeResult:
        best, best_eval = 0, float_info.min
        for gen in range(self._max_generations):
            print(f'Generation #:{gen}')
            scores = [c.fitness for c in self._pop]
            for i in range(self._population_count):
                if scores[i] > best_eval:
                    best, best_eval = self._pop[i], scores[i]
                    print(f"\tBest candidate citizen is {best}")
            selected = [GAChallengeBase._choose_breeder(self._pop, scores) for _ in range(self._population_count)]
            children = self._create_next_generation(breeders=selected)
            self._pop = children
            if best_eval >= self._fitness_threshold:
                print(f'I guess I found an acceptable solution (algorithm converged in {gen} generations)')
                break
        return GAChallengeResult(best, best_eval)


