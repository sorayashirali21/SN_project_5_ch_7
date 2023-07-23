
#49

import random


n = 10
num_iterations = 1000000


def generate_random_signed_graph():
    G = nx.complete_graph(n)
    for u, v in G.edges():
        sign = random.choice([-1, 1])
        G[u][v]['sign'] = sign
    return G


def run_dynamic_process(G):
    states = {n: random.choice([-1, 1]) for n in G.nodes()}
    for u, v in G.edges():
        sign = G[u][v]['sign']
        if sign == 1:
            if states[u] == states[v]:
                states[u] *= -1
            else:
                pass
        else:
            if states[u] == states[v]:
                pass
            else:
                states[v] *= -1
    return all(s == 1 for s in states.values())


num_balanced = 0
for i in range(num_iterations):
    G = generate_random_signed_graph()
    if run_dynamic_process(G):
        num_balanced += 1

frac_balanced = num_balanced / num_iterations
print(f"balance networks: {frac_balanced:.4f}")

'''result:
Fraction of balanced networks: 0.0010'''

num_balanced = 0
num_iterations = 100

for i in range(num_iterations):
    G = generate_random_signed_graph()
    if run_dynamic_process(G):
        num_balanced += 1

frac_balanced = num_balanced / num_iterations
print(f"networks: {frac_balanced:.20f}")

'''result:
Fraction of balanced networks: 0.01000000000000000021'''