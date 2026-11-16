
from itertools import product


kb = []

kb.append("P implies Q")
kb.append("P is True")


query = "Q"


print("Knowledge Base:")
for statement in kb:
    print(statement)

print("\nQuery:", query)

print("\nTruth Table:")
print("P  Q  KB  Query")

entailed = True

for P, Q in product([True, False], repeat=2):

    rule = (not P) or Q

    knowledge_base = rule and P

    print(P, Q, knowledge_base, Q)

    if knowledge_base and not Q:
        entailed = False


if entailed:
    print("\nKB entails the Query")
else:
    print("\nKB does not entail the Query")
