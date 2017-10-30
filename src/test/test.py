from engine.SeedTransducer import SeedTransducer
from engine import tsutil

sequence = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]
print(tsutil.signature_sequence(sequence))

lines = [line.rstrip('\n') for line in open('../input/seed_transducers.data')]
for line in lines:
    st = SeedTransducer(line)
