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

# Aim:
#     To implement crypt arithmetic problem of constraint satisfaction problem.
# Algorithm:
#     1) First, create a lilst of all the characters that need assigning to pass to solve.
#     2) Then make sure all the different characters have different number assigned to them. 
#     3) If the above steps is true then form the equation and append them to the list. 

