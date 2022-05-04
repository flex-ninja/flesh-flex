def solutions():
    # GO + TO = OUT
    all_solutions = list()
    for g in range(9, -1, -1):
        for o in range(9, -1, -1):
            for t in range(9, -1, -1):
                for u in range(9, -1, -1):
                    if len(set([g, o, t, u])) == 4:
                        go = 10 * g + o
                        to = 10 * t + o
                        out = 100 * o + 10 * u + t

                        if go + to == out:
                            all_solutions.append((go, to, out))
    return all_solutions

print(solutions())