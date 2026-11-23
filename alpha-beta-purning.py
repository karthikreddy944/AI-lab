
def alpha_beta(depth, node, maximizing, values, alpha, beta):

    if depth == 3:
        return values[node]

    if maximizing:
        best = -999

        for i in range(2):
            value = alpha_beta(depth + 1, node * 2 + i,
                               False, values, alpha, beta)

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = 999

        for i in range(2):
            value = alpha_beta(depth + 1, node * 2 + i,
                               True, values, alpha, beta)

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best


values = list(map(int, input("Enter 8 leaf values: ").split()))

if len(values) != 8:
    print("Please enter exactly 8 values")
else:
    result = alpha_beta(0, 0, True, values, -999, 999)
    print("Optimal value:", result)
