import sys

tasklist = []

pg1inpt = input("---------------------------------------------------------------\n\n--> Add task (press 1)\n--> View task (press 2)\n==> ")
print()
print("---------------------------------------------------------------")
print()

if pg1inpt == "1":
    # Read the existing tasks to determine the starting number
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            if lines:
                last_task = lines[-1]
                n = int(last_task.split('.')[0])
            else:
                n = 0
    except FileNotFoundError:
        n = 0

    print("(To stop adding task press Ctrl-Z)")
    print()
    while True:
        try:
            usrtask = input("Add task: ==> ")
            tasklist.append(usrtask)
        except EOFError:
            print()
            print("---------------------------------------------------------------")
            with open("tasks.txt", "a") as file:
                for line in tasklist:
                    n += 1
                    file.write(f"{n}. {line} []\n")
            break

elif pg1inpt == "2":
    try:
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
            for task in lines:
                print(task, end="")
            print()
            print("---------------------------------------------------------------")
            print()
    except FileNotFoundError:
        sys.exit("You haven't added a task yet :(\n\n---------------------------------------------------------------")

    try:
        task_number = int(input("Press task number of the task completed\n(If no task completed press ctrl-z)\n==> "))
        with open("tasks.txt", "r") as file:
            lines = file.readlines()
        
        with open("tasks.txt", "w") as file:
            for line in lines:
                if line.startswith(f"{task_number}."):
                    line = line.replace("[]", "[X]")
                file.write(line)
        
    except (EOFError, ValueError):
        print()
        sys.exit("Until next time :) ...\n---------------------------------------------------------------\n")
