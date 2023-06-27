# Do you find yourself writing code like this?


l = ["a", "b", "c", "d", "e"]
for i in range(len(l)):
    print(f"item #{i} is {l[i]}")

# Or maybe like this?

l = ["a", "b", "c", "d", "e"]
i = 0
for item in l:
    print(f"item #{i} is {item}")
    i += 1

# No need to worry, the stdlib is here to make your code cleaner.
# The enumerate function takes in any iterable, and converts it into an iterable
# that returns both the index, and the item. Turning the code above into this:

l = ["a", "b", "c", "d", "e"]
for i, item in enumerate(l):
    print(f"item #{i} is {item}")
