#!/usr/bin/env python
import os

import itertools
import shutil

names = open('filtered_names.txt').readlines()
names = [n.strip() for n in names]

images = os.listdir('images')
images = [i for i in images if i[0] != '.']
images.sort()

assert len(names) == len(images)

print zip(names, images)

try:
    os.makedirs('renamed_images')
except:
    pass

for name, image in zip(names, images):
    shutil.copyfile('images/{}'.format(image), 'renamed_images/{}.jpg'.format(name))

