def sort_by_name(people):
    return sorted(people, key=lambda person: person[0])

people_list = [("Maria", 22), ("João", 19), ("Ana", 25), ("Carlos", 20)]
result = sort_by_name(people_list)
print(result)
