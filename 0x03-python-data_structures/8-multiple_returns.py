#!/usr/bin/python3


def multiple_returns(sentence):
    if isinstance(sentence, str):
        length = len(sentence)
        if length == 0:
            First = None
        else:
            First = sentence[0]
        mult_tuple = (length, First)
        return (mult_tuple)
