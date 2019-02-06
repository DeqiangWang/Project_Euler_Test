# Utility 5
import numpy as np


# To obtain the elements in comp_array but not in main_array
def get_comp_array(main_arr, comp_arr):
    temp1 = np.sort(main_arr, axis=0, kind='mergesort', order=None)
    temp2 = np.sort(comp_arr, axis=0, kind='mergesort', order=None)
    idx = 0
    diff_el = []
    while idx != (len(main_arr) + len(comp_arr)):
        if (len(main_arr) == 0) or (len(comp_arr) == 0):
            print("Syntax Warning: One of the array is empty")
            return
        if temp1[0] == temp2[0]:
            diff_el.append(temp1[0])
            temp1 = np.delete(temp1, 0, None)
            temp2 = np.delete(temp2, 0, None)
            idx = idx + 1
            pass
        else:
            if temp1[0] > temp2[0]:
                diff_el.append(temp2[0])
                temp2 = np.delete(temp2, 0, None)
            else:
                diff_el.append(temp1[0])
                temp1 = np.delete(temp1, 0, None)
            idx = idx + 1

        if (len(temp1) == 0) or (len(temp2) == 0):
            diff_el = np.concatenate((diff_el, temp1), axis=None)
            diff_el = np.concatenate((diff_el, temp2), axis=None)
            return diff_el
    return diff_el





