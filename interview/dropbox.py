def recursive_count(network, curr_node):
    neighbors = network[curr_node];
    result = set();
    for index, connected in enumerate(neighbors):
        if connected == 1:
            result.add(index);
            network[curr_node][index] = 0;
            network[index][curr_node] = 0;
            result = result.union(recursive_count(network[:][:], index));
    return result;


def count(network, machine):
    n_copy = network[:][:];
    for i in range(len(network)):
        n_copy[i][i] = 0;

    result = recursive_count(n_copy, machine);
    result.add(machine);
    return len(result);

def repair_machine(network, initial_machines):
    initial_machines.sort();
    counts = [count(network, i) for i in initial_machines]
    print(initial_machines);
    print(counts);
    return [initial_machines[counts.index(max(counts))], max(counts)];

n = [   [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],#0
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],#1
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],#2
        [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],#3
        [0, 0, 0, 0 ,1, 1, 1, 0, 0, 0, 0],#4
        [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],#5
        [0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0],#6
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0],#7
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],#8
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],#9
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]];#10
m = [9,4, 0]
result = repair_machine(n,m);
print(result);
