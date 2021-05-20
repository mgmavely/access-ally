#finding-favorite-times
# total = 0
# for i in range(1,13):
#     for j in range(1,6):
#         for k in range(10):
#             if i >= 10:
#                 a = i//10
#                 b = i % 10
#                 if b-a == j-b == k-j:
#                     print(f"{i}:{j}{k}")
#                     total += 1
#             else:
#                 if j-i == k-j:
#                     print(f"{i}:{j}{k}")
#                     total += 1
# print(total)

# 31 times per 12 hour window as per function calculation above

minutes_observed = int(input("How long are you watching the lock [integer input required] "))
total = minutes_observed // 720 * 31 #we know how many times it happens every 12 hour interval, so we can save a lot of computation for large inputs and focus only on input % 720
minutes_observed %= 720
minutes_t = 6 #minutes value for tens column
minutes_o = 10 #minutes value for ones column
for i in range(0, (minutes_observed // 60) + 1):
    hour = 12 + i
    if hour > 12:
        hour -= 12
    if i == minutes_observed // 60:
            minutes_t = minutes_observed % 60 // 10 + 1
    for j in range(1,minutes_t):
        # print(minutes_o)
        if i == (minutes_observed // 60):
            minutes_o = minutes_observed % 10 + 1
        for k in range(minutes_o):
            if hour >= 10:
                a = hour//10
                b = hour % 10
                if b-a == j-b == k-j:
                    # print(f"{hour}:{j}{k}")
                    total += 1
            else:
                if j-i == k-j:
                    # print(f"{i}:{j}{k}")
                    total += 1
print(total)