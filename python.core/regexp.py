from common_func import print_start, print_end
import re
print_start()
# -------------- s t a r t ------------------------

regex = r"(\w+ (\d+))"

match = re.search(regex, "June 24")
print(match)

if match:
    for x in re.findall(regex, "June 24"):
        print(x)
else:
    print('No match')

# print("Full match:", match.group(0))


# ---------------- e n d ------------------------
print_end()
