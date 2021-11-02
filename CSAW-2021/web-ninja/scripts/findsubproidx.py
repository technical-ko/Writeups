f = open('list_of_subclasses.txt')
check = f.read()

for index,value in enumerate(check.split(',')):
    if "<class 'subprocess.Popen'>" in value:
        print(index)