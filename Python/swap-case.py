def swap_case(s):
    swapped = ''.join(list(map(lambda x : x.upper() if(x.islower()) else x.lower(), list(s))))
    return swapped

