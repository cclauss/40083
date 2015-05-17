import sys, collections

print(sys.argv[1])
with open(sys.argv[1], 'r') as f:
  elements = collections.Counter()
  for line in f:
    elements.update([line])
  print(len(list(elements)))
