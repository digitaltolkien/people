#!/usr/bin/env python3

import re

from collections import Counter
from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent
BIB_DIR = ROOT_DIR / "../awesome-sile-books/bibliographies/tolkien/"


authors = Counter()

for bib_file in BIB_DIR.glob("*/*.bib"):
    for line in open(bib_file):
        if m:= re.search(r"author\s*=\s*\{(.*?)\}", line):
            for author in m[1].split(" and "):
                authors[author.strip()] += 1

for author, _ in authors.most_common():
    print(author)
