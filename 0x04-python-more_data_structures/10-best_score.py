#!/bin/usr/python3

def best_score(a_dictionary):
    if a_dictionary:
        my_list = list(a_dictionary.keys())
        score = 0
        leader = ""
        for i in my_list:
            if a_dictionary[i] > score:
                socre = a_dictionary[i]
                leader = i
        return leader
