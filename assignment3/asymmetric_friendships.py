import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = [record[1], "is friended by"]
    mr.emit_intermediate(key, value)

    key = record[1]
    value = [record[0], "friended"]
    mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    friended = []
    friendedby = []
    for rel in list_of_values:
        if rel[1] == 'friended':
            friended.append(rel[0])
        elif rel[1] == 'is friended by':
            friendedby.append(rel[0])

    for f in friendedby:
        if f not in friended:
            mr.emit((key, f))

    for f in friended:
        if f not in friendedby:
            mr.emit((key, f))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
