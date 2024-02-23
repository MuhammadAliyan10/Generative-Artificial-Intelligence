def saveInformation(name,age,marks):
    passed = []
    failed = []
    permited = []
    notPermited = []
    passed.append(name) if marks > 90 else failed.append(name)
    permited.append(name) if age > 18 else notPermited.append(name)
    return passed, failed, permited, notPermited


name = input("Enter your name : ")
age = int(input("Enter your age : "))
marks = int(input("Enter your marks : "))

passed,failed,permited,notPermited = saveInformation(name,age,marks)

if len(passed) > 0:
    for p in passed :
        print("Passed : " + p)
if len(failed) > 0:
    for p in failed :
        print("Falied : " + p)
if len(permited) > 0:
    for p in permited :
        print("Permited : " + p)
if len(notPermited) > 0:
    for p in notPermited :
        print("Notpermited : " + p)
    