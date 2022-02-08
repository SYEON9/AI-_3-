#regular expression practice

string = \
        '''
        010-1234-1234
        010-1234-5678
        +82-10-5678-5678
        +82-4123-1234
        '''

pattern = r'^(?:0|\82-)\d{1,2}-(\d{4}0-\1$'

#regular expression practice

import re


for match in re.finditer(pattern, string, re.MULTILINE):
    print("전체 문자열", match.group(0))
    print(r"\1 문자열", match.group(1))


