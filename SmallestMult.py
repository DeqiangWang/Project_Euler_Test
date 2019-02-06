#Euler 5
import time
from utilities.util_get_lcd import get_lcd
from utilities.util_get_nat_sequence import get_count
import numpy as np


def main():
    startnum = 20
    subject_seq = np.flip(get_count(startnum))
    subject_num = startnum
    subject_seq = np.delete(subject_seq, 0, None)
    subject_seq = np.delete(subject_seq, -1, None)
    for num in subject_seq:
        subject_num = get_lcd(subject_num, num)
    return subject_num


start_time = time.time()
print(str(main()))
print("Time elapsed : " + str(time.time() - start_time))


