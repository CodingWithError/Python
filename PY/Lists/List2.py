my_list = []
next_number = 1

while True:
    print(f"The list is now {my_list}")
    action = input("a(d)d, (r)emove or e(x)it: ").lower()
    
    if action == "d":
        my_list.append(next_number)
        next_number += 1
    elif action == "r":
        if my_list:
            my_list.pop()
        else:
            print("The list is already empty!")
    elif action == "x":
        print("Bye!")
        break
    else:
        print("Invalid input, please enter 'd', 'r', or 'x'.")
