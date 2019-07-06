# import re
# your_love=re.match("wh","at are you doing? who is you mate?",re.I)
# if your_love:
#     print("you are my angle")
# else:
#     print("i lose you ")

import re
m=re.search(r'\w*som\w*','Where are you from? You look so handsome.',re.I)
if m:
    print(m.group(0))
else:
    print("not found")
