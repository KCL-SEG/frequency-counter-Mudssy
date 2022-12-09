"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    # Your code goes here
    for item in items:
        item =  str(item)
        if item in frequencies.keys():
            frequencies[item] +=1
        else:
            print(f'{item}')
            frequencies.update({item: 1})
    return frequencies
