
while True:
    want = input("1.append\n2.show\nChoose: ")

    if want == '1':
        name = input("write a name: ")
        number = input("write a number: ")

        with open("mokhatab.txt", "a") as notebook:
            notebook.write(f"{name} : {number}   /   ")
            
    elif want == '2':
        with open("mokhatab.txt", "r") as notebook:
            names = notebook.read()
            print(names)
            
    else:
        print("error")
       