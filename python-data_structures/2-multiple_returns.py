#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else None
    return length, first
sentence = "At Holberton School, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first)) 
