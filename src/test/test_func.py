from engine import time_series_util, features_code_generator
from . import constraint_function

#print(constraint_function.min_width_peak([4,4,2,2,3,5,5,6,3,1,1,2,2,2,2,2,2,1]))
#print(constraint_function.min_width_peak([7,5,5,1,4,5,2,2,3,5,6,2,3,3,3,1]))
print(constraint_function.min_surface_peak([7,5,5,1,4,5,2,2,3,5,6,2,3,3,3,1]))
print(constraint_function.min_max_peak([7,5,5,1,4,5,2,2,3,5,6,2,3,3,3,1]))
print(constraint_function.min_min_increasing([4,3,5,5,2,1,1,3,3,4,6,6,3,1,3,3]))