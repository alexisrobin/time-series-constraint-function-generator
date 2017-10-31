from engine import constraint_function_generator, time_series_util
from . import constraint_function
import time

sequence = [4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]
s_sequence = time_series_util.signature_sequence(sequence)
print(s_sequence)

constraint_function_generator.gen("./test/constraint_function.py")
time.sleep(2)
constraint_function.increasing(s_sequence)