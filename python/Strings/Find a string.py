import re
def count_substring(string, sub_string):
    match = re.findall('(?='+sub_string+')',string)
    return len(match)