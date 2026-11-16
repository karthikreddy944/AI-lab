
# Knowledge Base Creation
facts = ["Human(Ram)", "Human(Ravi)"]

rules = {
    "Mortal": ["Human"]
}

# Forward Chaining
def forward_chaining(query):
    new_facts = facts.copy()

    while True:
        added = False

        for result, conditions in rules.items():
            for fact in new_facts:
                for condition in conditions:
                    if fact.startswith(condition):
                        name = fact[ len(condition) + 1 : -1]
                        new_fact = result + "(" + name + ")"

                        if new_fact not in new_facts:
                            new_facts.append(new_fact)
                            added = True

        if not added:
            break

    print("Knowledge Base:", new_facts)

    if query in new_facts:
        print("Query is TRUE")
    else:
        print("Query is FALSE")


# Main Program
print("Initial Facts:", facts)

query = input("Enter your query: ")

forward_chaining(query)
