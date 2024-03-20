#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)

    if any(value is None for value in a_dictionary.values()):
        return (None)

    max_score = max(a_dictionary.items(), key=lambda item: item[1])
    return (max_score[0])
