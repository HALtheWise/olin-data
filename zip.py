#!/usr/bin/env python

import os

DO_MANUAL_CHECK = False

def get_possible_names():
    file = open('Olin Student Directory.txt')
    lines = file.readlines()
    lines = [l.strip() for l in lines]

    def isLikelyName(line):
        if '/' in line:
            return False
        if ',' in line:
            return False
        if len(line) <= 5:
            return False

        badPhrases = ['olin', 'college', 'student', 'directory', 'class of']

        for word in badPhrases:
            if line.lower().count(word):
                return False
        return True

    return filter(isLikelyName, lines)


def filter_names_by_user(names):
    newNames = []

    print "When presented with each name, type 'n' before pressing enter\n \
          if the name is invalid"
    for name in names:
        command = raw_input('"{}"? [y]/n : '.format(name))
        if command.lower() != 'n':
            newNames.append(name)

    return newNames


def save_names(names, file='filtered_names.txt'):
    f = open(file, 'w')
    f.writelines([n + '\n' for n in names])
    f.close()


def sanitize_names(names):
    names = [n.title() for n in names]
    return names


if __name__ == '__main__':
    names = get_possible_names()
    names = sanitize_names(names)
    if DO_MANUAL_CHECK:
        names = filter(names)

    save_names(names)
    print names, len(names)
