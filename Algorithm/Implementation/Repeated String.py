import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
s, n = input().strip(), int(input().strip())
print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))
