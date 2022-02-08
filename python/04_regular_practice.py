
#regular expression practice

import re
import 04_regular_expression

for match in re.finditer(pattern, string, re.MULTILINE):
    print("전체 문자열", match.group(0))
    print(r"\1 문자열", match.group(1))
