import time
import copy
import random
import numpy as np
from numpy.random import choice

from concurrent.futures import ProcessPoolExecutor
def ff(x):
    return x * x

def initialization_of_population(size, n_feat):
    # size: population size; n_feat: length of feature
    population = []
    for i in range(size):
        chromosome = list(range(240))
        np.random.shuffle(chromosome)
        population.append(chromosome)
    return population


def fitness_score(population):
    scores = []
    for chromosome in population:
        d = get_path_length(chromosome, point_dict)
        scores.append(d)
    
    inds = np.argsort(scores)
    # return by ascending order in terms of score
    return list(np.array(scores)[inds]), list(np.array(population)[inds])

def selection(pop_after_fit, score_after_fit, n_parents):
    population_nextgen, score_nextgen = [], []
    # for each same fitness score, keep at most 3 samples
    curr_score, curr_count = score_after_fit[0], -1
    for i, p in enumerate(pop_after_fit):
        if len(score_nextgen) > n_parents:
            break
        if curr_score == score_after_fit[i]:
            curr_count += 1
        else:
            curr_count = 0
            curr_score = score_after_fit[i]
        if curr_count < int(0.20 * n_parents) and len(population_nextgen) < n_parents:
            population_nextgen.append(pop_after_fit[i])
            score_nextgen.append(score_after_fit[i])
    # for i in range(n_parents):
    #    population_nextgen.append(pop_after_fit[i])
    
    # randomly add a few items only if not enough samples
    # print('find #:', len(score_nextgen))
    n_left = n_parents - len(score_nextgen)
    if n_left > 0:
        for i in range(n_left):
            j = random.randint(0, len(pop_after_fit)-1)
            population_nextgen.append(pop_after_fit[j])
            score_nextgen.append(score_after_fit[j])
    return score_nextgen[:n_parents], population_nextgen[:n_parents]


def rotate_at_value(chromosome, start_value):
    for i, v in enumerate(chromosome):
        if v == start_value:
            break
    chromosome = chromosome[i:] + chromosome[:i]
    return chromosome

def crossover(pop_after_select, n_feat):
    # expand pop for 3 times
    population_nextgen = copy.deepcopy(pop_after_select)
    # crossover. choose a random point to swap chromosome
    for i in range(len(pop_after_select)):
        j = random.randint(0, len(pop_after_select)-1)
        child1 = pop_after_select[i]
        child2 = pop_after_select[j]
        if not isinstance(child1, list):
            child1 = child1.tolist()
        if not isinstance(child2, list):
            child2 = child2.tolist()
        for num in range(2):
            # first s1 nodes to keep in child1
            s1 = random.randint(1, n_feat-2)
            r_nodes = [c for c in child2 if c in child1[s1:]]
            l_nodes = [c for c in child2 if c in child1[:s1]]
            # rotate l_nodes and r_nodes
            # print(len(child1), len(child2))
            r_nodes = rotate_at_value(r_nodes, child1[s1])
            l_nodes = rotate_at_value(l_nodes, child1[s1-1])
            l_nodes = l_nodes[::-1]
            
            child1 = child1[:s1] + r_nodes
            child2 = l_nodes + child1[s1:]
            population_nextgen.append(copy.deepcopy(child1))
            population_nextgen.append(copy.deepcopy(child2))
        
    return population_nextgen

def mutation(pop_after_cross, mutation_rate):
    # keep 20 parent + make 80 mutations
    population_nextgen = copy.deepcopy(pop_after_cross)
    # for w in range(0,10):
    for i in range(0, len(pop_after_cross)):
        c0 = pop_after_cross[i]
        if not isinstance(c0, list):
            c0 = c0.tolist()
        chromosome = copy.deepcopy(c0)
        # rotate before mutation
        r = random.randint(0, len(chromosome)-1)
        c0 = chromosome[r:] + chromosome[:r]
        chromosome = copy.deepcopy(c0)
        for j in range(len(chromosome)):
            if random.random() < mutation_rate and j>=2:
                # swap j with j-1
                temp = chromosome[j-1]
                chromosome[j-1] = chromosome[j]
                chromosome[j] = temp
                population_nextgen.append(copy.deepcopy(chromosome))
                chromosome = copy.deepcopy(c0)
        
        chromosome = copy.deepcopy(c0)
        for j in range(len(chromosome)):
            if random.random() < mutation_rate and j>=2 and j <= len(chromosome)-2:
                # swap j with k, k corresponds to a neighbor
                k_id, k = choice(indices[j], p=prob[j]), 1
                for k, c_id in enumerate(chromosome):
                    if c_id == k_id:
                        break
                # print(k, k_id, chromosome[k])
                temp = chromosome[k]
                chromosome[k] = chromosome[j+1]
                chromosome[j+1] = temp
                population_nextgen.append(copy.deepcopy(chromosome))
                chromosome = copy.deepcopy(c0)
        
        # another kind of swap (swap both ends for same chromosome)
        for j in range(len(chromosome)):
            if random.random() < mutation_rate and j>=2 and j <= len(chromosome)-2:
                # swap j with k, k corresponds to a neighbor
                k_id, k = choice(indices[j], p=prob[j]), 1
                for k, c_id in enumerate(chromosome):
                    if c_id == k_id:
                        break
                # print(k, k_id, chromosome[k])
                k, j = min(k,j), max(k,j)
                l, r = chromosome[:k], chromosome[j:]
                mid = chromosome[k:j]
                chromosome = l + mid[::-1] + r
                
                population_nextgen.append(copy.deepcopy(chromosome))
            
    return population_nextgen


def generations(size, n_feat, n_parents,
                mutation_rate, n_gen, init_population=None,
                verbose = True):
    best_chromo = []
    best_score  = []
    if init_population is not None:
        population_nextgen = init_population
    else:
        population_nextgen = initialization_of_population(size, n_feat)
    # step 2-5
    for i in range(n_gen):
        scores, pop_after_fit = fitness_score(population_nextgen)
        scores, pop_after_sel = selection(pop_after_fit, scores, n_parents)
        if verbose:
            print('generation: {} ; original population: {}, after selection is: {}'\
                  .format(i, len(pop_after_fit), len(pop_after_sel)))
            print(scores[:17])
        if i % 50 == 0:
            print('generation: {} ; original population: {}, after selection is: {}'\
                  .format(i, len(pop_after_fit), len(pop_after_sel)))
            print(scores[:17])
        # print('pop_after_sel', pop_after_sel)
        pop_after_cross = crossover(pop_after_sel, n_feat)
        # print('pop_after_cross', len(pop_after_cross))
        population_nextgen = mutation(pop_after_cross, mutation_rate)
        # print('population_nextgen', len(population_nextgen))
        best_chromo.append(pop_after_fit[0])
        best_score.append(scores[0])
    last_chromo = population_nextgen
    return best_chromo, best_score, last_chromo


def run_iterate(data_dict):
    t0 = time.time()
    for k, v in data_dict.items():
        globals()[k] = v
    last_chromo = data_dict['last_chromo']
    best_records, best_scores = [], []
    
    while True:
        best_chromo, best_score, last_chromo = \
        generations(size = 100, n_feat = 240, n_parents=100,
                   mutation_rate=0.01, n_gen=100,
                   init_population = last_chromo, verbose = False)
        best_records = best_records + best_chromo
        best_scores = best_scores + best_score
    
        if time.time() - t0 > 3600 * 2:
            return best_records, best_scores
    return best_records, best_scores


def pool_STP_map(nprocs, data_dict):
    # Let the executor divide the work among processes by using 'map'.
    with ProcessPoolExecutor(max_workers=nprocs) as executor:
        rets = executor.map(run_iterate, [data_dict for i in range(nprocs)])
        return rets

def get_distance(x1,y1,x2,y2):
    return abs(x1-x2) + abs(y1-y2)

def get_path_length(pts_order, point_dict):
    p_start = point_dict[pts_order[0]]
    p0 = p_start
    
    all_dist = 0
    for i in range(1, len(pts_order)):
        p1 = point_dict[pts_order[i]]
        all_dist += get_distance(p0[0], p0[1], p1[0], p1[1])
        p0 = p1
    all_dist += get_distance(p0[0], p0[1], p_start[0], p_start[1])
    return all_dist



