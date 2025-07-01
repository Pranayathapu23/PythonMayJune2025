""" 
Purpose : print() function syntax and usage
    Escapes sequences
        -characters whose presence is felt but they cant print
         \t - tab space
         \n - new line
         \b - raw string


"""


print("hello world python")
print("hello \tworld \tpython")
print("hello \tworld \npython")

print("hello", "world", 12345, end="\t")
print("hello", "world", 12345, end="\t", sep=";")

