from random import randint, random


def crossover(parent_1: list, parent_2: list, crossover_rate: float):
    """
    the crossover operator takes two parents to create two children with potential DNA mix-up
    :param parent_1: the first parent's genetic material (as a list of bits)
    :param parent_2: the second parent's genetic material (as a list of bits)
    :param crossover_rate: the probability at which cross-over will be occurring
    :return: a list of 2 children whose genetic material is composed of a random mix of the ones from their parents
    """
    child_1, child_2 = parent_1.copy(), parent_2.copy()
    # should we perform genome mix-up off the 2 parents?
    if random() < crossover_rate:
        # choose a crossing point where we'll be splitting up the genetic material
        pt = randint(1, len(parent_1)-2)
        # take a first bit of the first parent_1 then the rest of the DNA from parent_2
        child_1 = parent_1[:pt] + parent_2[pt:]
        child_2 = parent_2[:pt] + parent_1[pt:]
    return [child_1, child_2]


def mutation(dna: list, mutation_rate: float):
    """
    the mutation operator takes the DNA from an individual and eventually mutate a gene.
    (mutating a gene means flipping the corresponding bit as the genes are bool)
    :param dna: the genetic material candidate for being muted
    :param mutation_rate: the probability at which mutation will be occurring
    :return: the new dna which may have muted (or not)
    """
    for i in range(len(dna)):
        # should we perform mutation?
        if random() < mutation_rate:
            # flip the bit
            dna[i] = 1 - dna[i]


def selection(pop: list, scores, k=3):
    """
    the selection operator selects one citizen who will become a parent to breed next generation
    :param pop: the population as a list of citizen (each citizen is in turn modeled by its dna as a list of bits)
    :param scores: the citizen's fitness (as a list of float)
    :param k: the number of citizen to compare the fitness with
    :return: the 'happy' citizen that will have a chance to become a parent
    """
    # first random selection
    selection_ix = randint(0, len(pop) - 1)
    for _ in range(k):
        ix = randint(0, len(pop) - 1)
        # check if better (e.g. perform a tournament)
        if scores[ix] > scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]


def darwin(
        init_population_fn,
        fitness_fn,
        fitness_threshold: float,
        decode_fn,
        population_count: int = 150,
        genome_size: int = 16,
        max_generations: int = 100,
        crossover_rate: float = 0.9,
        mutation_rate: float = 0.05):
    """
    This is the entry point of the genetic algorithm, where all the magic occurs.
    It mimics the natural species evolution where the most adapted (who has best fitness) has more chance to reproduce.
    It also introduces cross-over (mix-up of the parent's DNA) and eventual mutations.
    The cross-over and mutation operators occur with a configurable probability.
    The random noise introduced by the cross-over / mutation / selection operators is key to get a stochastic approach.
    This allows the algorithm to also explore some totally different corners of the entire research space.
    :param init_population_fn:
    :param fitness_fn:
    :param fitness_threshold:
    :param decode_fn:
    :param population_count:
    :param genome_size:
    :param max_generations:
    :param crossover_rate:
    :param mutation_rate:
    :return:
    """
    def create_next_generation(population: list, crossover_probability: float, mutation_probability: float):
        """create the next generation"""
        new_children: list = []
        for j in range(0, len(population) - 1, 2):
            # take a pair of citizen that will become new parents
            citizen_1, citizen_2 = population[j], population[j + 1]
            # to introduce noise and mimic natural evolution, perform crossover and mutation on the newly born children
            for c in crossover(citizen_1, citizen_2, crossover_probability):
                mutation(c, mutation_probability)
                new_children.append(c)
        return new_children

    pop = init_population_fn(population_count=population_count, genome_size=genome_size)
    # keep track of best solution
    best, best_eval = 0, fitness_fn(pop[0])
    # enumerate generations
    for gen in range(max_generations):
        print(f'Generation #:{gen}')
        # evaluate all candidates in the population
        scores = [fitness_fn(c) for c in pop]
        # check for new best solution
        for i in range(population_count):
            if scores[i] > best_eval:
                best, best_eval = pop[i], scores[i]
                binary_dna = ''.join(str(gene) for gene in pop[i])
                print(f"\tFound a better candidate citizen (fitness={scores[i]:4} and DNA={binary_dna})")
        # select parents
        selected = [selection(pop, scores) for _ in range(population_count)]
        # create the next generation
        children = create_next_generation(population=selected,
                                          crossover_probability=crossover_rate,
                                          mutation_probability=mutation_rate)
        # replace population
        pop = children
        # if our best fitness (best_eval) is >= than the targeted one (fitness_threshold)
        if best_eval >= fitness_threshold:
            print(f'I guess I found an acceptable solution (algorithm converged in {gen} generations)')
            break
    return [best, best_eval]