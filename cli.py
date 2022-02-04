
import base

while True:
    inp = input("Enter a command: ")
    if inp == "exit":
        break
    else:
        base.main(inp)
        print(base.main.respn)
