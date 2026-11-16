
# Unification in First Order Logic

def unify(x, y, substitution):

    if x == y:
        return substitution

    if isinstance(x, str) and x.islower():
        substitution[x] = y
        return substitution

    if isinstance(y, str) and y.islower():
        substitution[y] = x
        return substitution

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0]:
            return None

        for a, b in zip(x[1:], y[1:]):
            substitution = unify(a, b, substitution)

            if substitution is None:
                return None

        return substitution

    return None


# Main Program
x = ("Knows", "x", "John")
y = ("Knows", "Mary", "John")

result = unify(x, y, {})

print("First Expression:", x)
print("Second Expression:", y)

if result is not None:
    print("Unification Successful")
    print("Substitution:", result)
else:
    print("Unification Failed")
