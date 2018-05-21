

#循环loop 有限循环、无限循环、死循环

#i代表每循环自定加1 range
# for i in  range(3):
#     print(i)

#2位步长
# for i in range(1, 100,2):
#     print(i)

# for i in range(100):
#     if i < 50 or i >70:
#         print(i)

# count = 0
# while True:
#     if count > 2**10:
#         break
#
#     count += 1

for i in  range(10):
    if i < 5:
        continue

    print(i)

