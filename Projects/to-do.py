s = []

while (True):
    op = int(input(('''
          Select your current operation:
          1. Add a Task
          2. View your Tasks
          3. Remove your last task
          4. exit
          ''')))
    if op == 1:
       task = input("Enter the task you want to add: ")
       s.append(task)
    elif op == 2:
        print(s)
    elif op == 3:
        if s:
            s.pop()
        else:
            print("There is no task to remove")
    elif op == 4:
        break
    else : 
        print("Enter a valid input.")