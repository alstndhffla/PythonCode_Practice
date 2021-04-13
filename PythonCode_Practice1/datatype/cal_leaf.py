"""
https://ko.khanacademy.org/math/statistics-probability/displaying-describing-data/quantitative-data-graphs/v/u08-l1-t2-we3-stem-and-leaf-plots

"""

score = [0, 0, 2, 4, 7, 7, 9]
score += [11, 11, 13, 18]
score += [20]

stem_leaf = [[], [], []]

# ex 1

for s in score:
    d, m = divmod(s, 10)
    stem_leaf[d].append(m)

# ex 2

for i in range(len(stem_leaf)):
    print(f'{i}: {stem_leaf[i]}')