from engine import time_series_util, features_code_generator
from . import constraint_function
import time

def timeAndValidateFunc(f, arg, ouput):
    time1 = time.time()
    ret = f(arg)
    time2 = time.time()
    print('\n')
    print('TEST %s' % (f.__name__))
    if ouput == ret:
        print('=> PASS')
    else:
        print('=> FAIL')
    print('=> function should return %d and return %d' % (ouput, ret))
    print('=> function took %0.3f ms' % ((time2-time1)*1000.0))
    return ret

sequence1 = [7,5,5,1,4,5,2,2,3,5,6,2,3,3,3,1]
sequence2 = [4,3,5,5,2,1,1,3,3,4,6,6,3,1,3,3]
sequence3 = [4,1,3,1,4,6,1,5,5,2,7,2,3,1,6,1]
sequence4 = [1,7,3,4,4,5,5,4,2,2,6,5,4,6,5,7]
sequence5 = [4,4,6,4,1,1,3,4,4,6,6,5,2,2,4,3]
sequence6 = [1,2,3,2,5,6,7,4,1,3,4,6,1,2,4,4]
sequence7 = [1,2,6,6,4,4,3,5,2,5,1,5,3,3,4,4]
sequence8 = [3,4,2,2,5,6,6,4,4,3,1,1,4,6,4,4]

timeAndValidateFunc(constraint_function.min_surface_peak, sequence1, 9)
timeAndValidateFunc(constraint_function.min_max_peak, sequence1, 3)
timeAndValidateFunc(constraint_function.min_min_increasing, sequence2, 1)
timeAndValidateFunc(constraint_function.max_range_increasing, sequence2, 2)
timeAndValidateFunc(constraint_function.max_range_increasing_sequence, sequence8, 5)
timeAndValidateFunc(constraint_function.sum_surface_zigzag, sequence3, 33)
timeAndValidateFunc(constraint_function.min_min_gorge, sequence4, 3)
timeAndValidateFunc(constraint_function.max_surface_strictly_decreasing_sequence, sequence5, 13)
timeAndValidateFunc(constraint_function.min_max_dip_on_increasing_sequence, sequence6, 5)
timeAndValidateFunc(constraint_function.min_max_inflexion, sequence7, 1)