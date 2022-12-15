test = list("gpijregijergre")
i = 0

while i < len(test):
    print(len(test))
    if "i" in test:
        test.remove("i")
    i += 1

# output:
# 14
# 13
# 12
# 12
# 12
# 12
# 12
# 12
# 12
# 12
# 12
# 12
