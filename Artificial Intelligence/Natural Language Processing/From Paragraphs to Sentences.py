import re
para = input()

pattern = re.compile(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s')

for sentence in re.split(pattern,para):
    print(sentence)