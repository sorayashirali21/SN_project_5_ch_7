# 48

num_of_edges = G.number_of_edges()
num_of_positive_edges = sum([1 for (_, _, sign) in G.edges(data='sign') if sign > 0])
num_of_negative_edges = sum([1 for (_, _, sign) in G.edges(data='sign') if sign < 0])
frac_positive_edges = num_of_positive_edges / num_of_edges
frac_negative_edges = num_of_negative_edges / num_of_edges

print(f"positive edges: {frac_positive_edges}")
print(f"negative edges: {frac_negative_edges}")

'''result:
Fraction of positive edges: 0.8324882724088661
Fraction of negative edges: 0.1675117275911338'''
