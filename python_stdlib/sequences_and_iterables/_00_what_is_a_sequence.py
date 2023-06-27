# What is a sequence?
# A sequence is an "iterator" which implements the __getitem__() and __len__() methods.

# What is an iterator?
# An iterator is an object which implements either the __iter__() method or both
# the __next__() and __iter__() methods.

# Built in examples of sequences are Lists, Sets, and Tuples.
# All sequences are iterators, but not all iterators are sequences

# Now lets build a sequence object, to do so we are going to need to implement a
# class with at least: __getitem__(), __len__(), and __iter__() methods.


# To keep things simple, this sequence will contain the characters a, b, and c and nothing more.
from typing import Iterator, Union


class ABCSequence:
    def __iter__(self) -> Iterator[str]:
        """
        The __iter__ method must return an iterator, which often is just the object itself.
        Because we want this iterator to always return a, b, and then c. We will use the yield
        syntax to do just that. When `next` is called on this iterable object this method will execute
        until it encounters the first yield statement, where it will pause until `next` is called again.

        By utilizing the `yield` syntax python has automatically implemented __next__ for this iterable.
        """
        yield "a"
        yield "b"
        yield "c"

    def __getitem__(self, key: Union[int, slice]) -> str:
        """
        The __getitem__ signature for sequences requires us to implement the method for both an
        integer key and a slice key.

        Because this sequence will always contain the characters a, b, and c in that order
        it is trivial to implement the integer method with a simple if/else.
        """
        if isinstance(key, int):
            if key == 0:
                return "a"
            elif key == 1:
                return "b"
            elif key == 2:
                return "c"
            else:
                raise IndexError(f"{key} is out of range of the ABCSequence.")
        if isinstance(key, slice):
            """
            Because this object does not support not being a sequence of a, b,
            and c we will not support slice objects.
            """
            raise NotImplementedError("Cannot return a slice of the ABCSequence.")

    def __len__(self) -> int:
        """
        This one is easy, this is a fixed length sequence so we can always return 3.
        """
        return 3


# Now that we have our sequence object, let's test it out.
abc_sequence = ABCSequence()

print("Lets try and print out the sequence using a for statement.")
for o in abc_sequence:
    print(o)

print("Lets get sequence items by index.")
print(abc_sequence[0])
print(abc_sequence[1])
print(abc_sequence[2])

print("Lets get the sequence items in reverse.")
for o in reversed(abc_sequence):
    print(o)

print("Lets see if 'a' is in our sequence using the in operator")
print("a" in abc_sequence)

print("Lets see if 'z' is in our sequence using the in operator")
print("z" in abc_sequence)

print("Lets see if we can add two of our sequences together")
try:
    print(abc_sequence + abc_sequence)
except Exception as e:
    print(
        f"Oops, that didn't work. We didn't implement a way to concatenate two of our sequences together."
    )

print("Lets see if we can use max() and min() with our sequence.")
print(f"max: {max(abc_sequence)} min: {min(abc_sequence)}")

print("Lets see if we can get the length of the sequence using len()")
print(f"len: {len(abc_sequence)}")

print(
    "Lets see if we can use the .index() method for our sequence to find the first occurrence of b."
)
try:
    print(abc_sequence.index("b"))
except Exception as e:
    print(f"Oops, that didn't work. Our sequence object doesn't implement that method.")

print("Lets get a subset of the sequence using the slice operator.")
try:
    print(abc_sequence[:2])
except Exception as e:
    print(
        f"Oops, that didn't work. Our __getitem__ method doesn't support slices:\n {e}"
    )

# Built in sequence types like Lists, Sets, and Tuples all implement the needed methods as well as many more.
# Now lets see how a tuple containing the characters a, b, and c does in the same tests we did in on ur object.
abc_sequence = ("a", "b", "c")

print("Lets try and print out the sequence using a for statement.")
for o in abc_sequence:
    print(o)

print("Lets get sequence items by index.")
print(abc_sequence[0])
print(abc_sequence[1])
print(abc_sequence[2])

print("Lets get the sequence items in reverse.")
for o in reversed(abc_sequence):
    print(o)

print("Lets see if 'a' is in our sequence using the in operator")
print("a" in abc_sequence)

print("Lets see if 'z' is in our sequence using the in operator")
print("z" in abc_sequence)

print("Lets see if we can add two of our sequences together")
try:
    print(abc_sequence + abc_sequence)
except Exception as e:
    print(
        f"Oops, that didn't work. We didn't implement a way to concatenate two of our sequences together."
    )

print("Lets see if we can use max() and min() with our sequence.")
print(f"max: {max(abc_sequence)} min: {min(abc_sequence)}")

print("Lets see if we can get the length of the sequence using len()")
print(f"len: {len(abc_sequence)}")

print(
    "Lets see if we can use the .index() method for our sequence to find the first occurrence of b."
)
try:
    print(abc_sequence.index("b"))
except Exception as e:
    print(f"Oops, that didn't work. Our sequence object doesn't implement that method.")

print("Lets get a subset of the sequence using the slice operator.")
try:
    print(abc_sequence[:2])
except Exception as e:
    print(
        f"Oops, that didn't work. Our __getitem__ method doesn't support slices:\n{e}"
    )

# It seems to have passed all of the tests, even the ones that our sequence didn't
# because it can actually return a slice, implements the __index__ method, and can be concatenated.
