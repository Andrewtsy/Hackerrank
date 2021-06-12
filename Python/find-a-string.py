def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        try:
            if string[i: i + len(sub_string)] == sub_string:
                count += 1
        except:
            pass
    return count

