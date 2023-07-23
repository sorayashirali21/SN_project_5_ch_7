import gzip
import networkx as nx

# 47

G = nx.read_edgelist('soc-sign-epinions.txt', delimiter='\t', data=[('sign', int)], create_using=nx.Graph())

triangles = sum(nx.triangles(G).values())
total_triads = triangles // 3

for triad in range(1, 17):
    print(f"Triad {triad}:/{total_triads}")

'''result:Triad 1: count = 1, fraction = 1/4910076
Triad 2: count = 1, fraction = 1/4910076
Triad 3: count = 1, fraction = 1/4910076
Triad 4: count = 1, fraction = 1/4910076
Triad 5: count = 1, fraction = 1/4910076
Triad 6: count = 1, fraction = 1/4910076
Triad 7: count = 1, fraction = 1/4910076
Triad 8: count = 1, fraction = 1/4910076
Triad 9: count = 1, fraction = 1/4910076
Triad 10: count = 1, fraction = 1/4910076
Triad 11: count = 1, fraction = 1/4910076
Triad 12: count = 1, fraction = 1/4910076
Triad 13: count = 1, fraction = 1/4910076
Triad 14: count = 1, fraction = 1/4910076
Triad 15: count = 1, fraction = 1/4910076
Triad 16: count = 1, fraction = 1/4910076 '''
