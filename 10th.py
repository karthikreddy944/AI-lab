


import re


def remove_implication(expr):
    expr = re.sub(r'(\w+\(.*?\))\s*->\s*(\w+\(.*?\))',
                  r'(~\1 | \2)', expr)
    return expr



def remove_quantifier(expr):
    expr = re.sub(r'Forall\s+\w+\s*', '', expr)
    return expr



def convert_to_cnf(expr):
    print("Original Expression:", expr)

    expr = remove_implication(expr)
    print("After removing implication:", expr)

    expr = remove_quantifier(expr)
    print("After removing quantifier:", expr)

    print("Final CNF:", expr)


expression = "Forall x (P(x) -> Q(x))"

convert_to_cnf(expression)
