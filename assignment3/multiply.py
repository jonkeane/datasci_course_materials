import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

N = 4
L = 4

def mapper(record):
    # key: document identifier
    # value: document contents
    if record[0] == "a":
        for k in range(0,N+1):
            key = (record[1],k)
            value = ['a', record[3]]
            mr.emit_intermediate(key, record)

    if record[0] == "b":
        for k in range(0,L+1):
            key = (k, record[2])
            value = ['b', record[3]]
            mr.emit_intermediate(key, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    a = {}
    b = {}
    for val in list_of_values:
        if val[0] == 'a':
            a[val[2]] = val[3]
        elif val[0] == 'b':
            b[val[1]] = val[3]

    # print(key)
    # print(a)
    # print(b)

    out = []
    for i in range(0, N+1):
        try:
            out.append(a[i]*b[i])
        except KeyError as e:
            pass

    mr.emit((key[0], key[1], sum(out)))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
