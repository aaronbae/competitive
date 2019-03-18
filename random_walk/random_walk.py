import matplotlib.pyplot as plt
import random as r
import time

def generate_sequence(size, p, starting_val=0):
    s = [starting_val];
    r.seed(time.time());
    for i in range(1, size):
        if r.random() < p:
            starting_val += 1
        else:
            starting_val -= 1
        s.append(starting_val)
    return s

def graph_png(file_name, sequence):
    print(sequence);
    plt.figure(1)
    plt.plot(sequence)
    plt.xlabel('Time (t)')
    plt.ylabel('Random Walk Location')
    plt.title('Random Walk Simulated')
    plt.savefig(file_name);
    plt.close();

def graph_multiple_sequences(file_name, num_walks, length, p):
    plt.figure(1);
    plt.xlabel('Time (t)')
    plt.ylabel('Random Walk Location')
    plt.title('Random Walk Simulated')
    for i in range(num_walks):
        s = generate_sequence(length, p);
        plt.plot(s);
    plt.savefig(file_name);
    plt.close();

graph_multiple_sequences("new_graph.png", 5, 10000, 0.5);
