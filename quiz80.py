
daily = {b for c in range(10) for b in range(c)};
for coding in range(0, len(daily)):
    if coding == 0:
        habit = 24
    else:
        habit -= 2
print(habit)

# 8