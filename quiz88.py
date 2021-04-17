

daily = ["***", "*", "", "****", "*****"]
for coding, habit in enumerate(daily, start=1):
    if int(int(coding)*1.5) != 2:
        if min(abs(coding), abs(-2.5)) %2 == 0:
            print("{}".format(habit*coding))
    


# **