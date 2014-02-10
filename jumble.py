#!/usr/bin/python

import sys

def countletters(word):
    lettercounts = {}
    for letter in word:
        if letter in lettercounts:
            lettercounts[letter]=lettercounts[letter]+1
        else:
            lettercounts[letter]=1
    return lettercounts


def main(argv):
    word = str(argv)
    lettercounts = countletters(word) 
    with open('corncob_lowercase.txt') as file:
        for line in file:
            linestr = line.rstrip()
            linelettercounts = countletters(linestr)
	    anagram = True
            for letter in linelettercounts:
		if letter not in lettercounts:
		    anagram = False
                elif linelettercounts[letter]>lettercounts[letter]:
	            anagram = False
            if anagram:
                print linestr


if __name__ == "__main__":
    main(sys.argv[1])
