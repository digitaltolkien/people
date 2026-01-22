# People DB

This is just a proof-of-concept exploring putting together an authority list
of primary-world people for the Tolkien Linked Open Data Project.

I have initially gathered:
  - entries from Scull and Hammond’s Reader’s Guide
  - authors from Le Dragon de Brume’s bibliography
  - artists from the TCG Guide to Calendars
  - senders and recipients from the TCG Guide to Letters
  - people in the index to Carpenter’s Biography

The raw lists can be found in `raw-lists` (the bibliography authors extracted
using `scripts/convert-bibl.py`)

Since then, Le Dragon de Brume has produced `raw-lists/names-biblio.yaml`.

An initial merge was done with `scripts/merge.py` to produce `merged.txt` which
We are manually inspecting and editing to group likely duplicates with
alternative names (or, in some cases, typos).

We have taken a first pass through surnames beginning with A through N.

This data is made available under a [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.

To discuss or contribute, please join our Discord (link on
<https://digitaltolkien.com/>) and ping us in the `#linked-open-data` channel.
