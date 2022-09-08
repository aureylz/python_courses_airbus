from typing import Callable

def fill_knapsack(problem: KnapsackProblem, strategy: Callable)->KnapsackSolution:
    sorted_index_items = sorted(range(len(problem.list_items)), 
                                key=lambda x: strategy(problem.list_items[x]))
    knapsol = [False for i in range(len(problem.list_items))]
    current_weight = 0
    for j in range(len(sorted_index_items)):
        if current_weight+problem.list_items[sorted_index_items[j]]["weight"]<=problem.max_capacity:
            knapsol[sorted_index_items[j]]=True
            current_weight += problem.list_items[sorted_index_items[j]]["weight"]
    return KnapsackSolution(knapsol)

