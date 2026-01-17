#!/usr/bin/env python3

from collections import defaultdict
from pathlib import Path


ROOT_DIR = Path(__file__).parent.parent
RAW_LISTS_DIR = ROOT_DIR / "raw-lists"


people = defaultdict(list)

for num, line in enumerate(open(RAW_LISTS_DIR / "bibliography-authors.txt"), 1):
    person = line.strip()
    if person:
        people[person].append(f"biblio-{num}")

for line in open(RAW_LISTS_DIR / "scull-and-hammond-guide.txt"):
    person = line.strip()
    if person:
        people[person].append(f"scull-and-hammond")

for num, line in enumerate(open(RAW_LISTS_DIR / "tcg-calendar-artists.txt"), 1):
    person = line.strip()
    if person:
        person = person.split()[-1] + ", " + " ".join(person.split()[:-1])
        people[person].append(f"artists-{num}")

for num, line in enumerate(open(RAW_LISTS_DIR / "tcg-letters-from.txt"), 1):
    person = line.strip()
    if person:
        person = person.split()[-1] + ", " + " ".join(person.split()[:-1])
        people[person].append(f"letters-from-{num}")

for num, line in enumerate(open(RAW_LISTS_DIR / "tcg-letters-to.txt"), 1):
    person = line.strip()
    if person:
        person = person.split()[-1] + ", " + " ".join(person.split()[:-1])
        people[person].append(f"letters-to-{num}")


for person in sorted(people):
    print(person)
    for source in people[person]:
        print(f"    {source}")
