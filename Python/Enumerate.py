marks = [30,54,67,87,23,53,12,54,54]

# index = 0
# for mark in marks:
#     print(mark)
#     if(index == 3):
#         print("WoW")
#     index +=1

#! Now we are using enumerate function

for index,mark in enumerate(marks):
    print(index,mark)