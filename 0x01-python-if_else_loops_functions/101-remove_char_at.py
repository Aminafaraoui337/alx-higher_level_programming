#!/usr/bin/python3
def remove_char_at(str, n):
    wantedstr = ""
    for i, c in enumerate(str):
        if i != n:
            wantedstr += c
    return wantedstr
