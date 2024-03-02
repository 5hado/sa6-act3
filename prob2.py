names = ["Ethan", "Olivia", "Liam", "Emma", "Noah", "Ava", "Lucas", "Isabella", "Mason", "Sophia"]

sorted_strings = sorted(names, key=lambda x: (len(x), x))

print(sorted_strings)