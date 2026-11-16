
# Knowledge Base using Propositional Logic

# Clauses in CNF
kb = [
    {"~P", "Q"},   # P -> Q
    {"P"}          # P is true
]

# Given query
query = "Q"

# Negate the query
negated_query = "~" + query

kb.append({negated_query})

print("Knowledge Base:", kb)
print("Negated Query:", negated_query)

# Resolution function
def resolve(c1, c2):
    new_clauses = set()

    for literal in c1:
        if literal.startswith("~"):
            opposite = literal[1:]
        else:
            opposite = "~" + literal

        if opposite in c2:
            new_clause = (c1 - {literal}) | (c2 - {opposite})
            new_clauses.add(frozenset(new_clause))

    return new_clauses


# Resolution process
clauses = set(frozenset(c) for c in kb)

while True:
    new_clauses = set()
    clause_list = list(clauses)

    for i in range(len(clause_list)):
        for j in range(i + 1, len(clause_list)):
            result = resolve(clause_list[i], clause_list[j])

            if frozenset() in result:
                print("Empty clause obtained!")
                print("Query is PROVED using Resolution")
                exit()

            new_clauses.update(result)

    if new_clauses.issubset(clauses):
        print("Query cannot be proved")
        break

    clauses.update(new_clauses)
