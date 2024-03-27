'''
while True:
    try:
        n = int(input("please enter an integer:"))
        m = int(input("please enter an integer:"))
        z = n / m
        break
    except Exception as e:
        print("not an integer! please try again 123")
        print(e)
    except ValueError:
        print("not an integer! please try again 456")
    finally:
        print("you successfully entered an integer!")
'''

try:
    klu1 =open("file.txt","r+")
    try:
        klu1.write("xyz This is S11 Section CRT Class")
    finally:
        klu1.close()
except IOError:
    print("File Not Found")
else:
    print("The file opened successfully")
    klu1.close()