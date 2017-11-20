from engine import time_series_util, features_code_generator
from . import constraint_function

sequence = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]
s_sequence = time_series_util.signature_sequence(sequence)
print(s_sequence)
print(constraint_function.min_width_increasing(s_sequence))
print(constraint_function.min_width_peak(s_sequence))