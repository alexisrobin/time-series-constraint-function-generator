from engine import time_series_util, features_code_generator
from . import constraint_function
import time

def timeAndValidateFunc(f, arg, ouput):
    time1 = time.time()
    ret = f(arg)
    time2 = time.time()
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

timeAndValidateFunc(constraint_function.min_surface_peak, sequence1, 9)
timeAndValidateFunc(constraint_function.min_max_peak, sequence1, 3)
timeAndValidateFunc(constraint_function.min_min_increasing, sequence2, 1)
timeAndValidateFunc(constraint_function.max_range_increasing, sequence2, 2)