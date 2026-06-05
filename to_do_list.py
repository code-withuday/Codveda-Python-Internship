                                                                       #---- TO DO LIST ----
tasks = []                                                                     

while True:
    print("\n--to do list--")
    print("add task")
    print("view task")
    print("view exit")
    
    
    Choice = int(input("enter choice: "))
    

    if(Choice == 1):
        task = input("enter tasks: ")
        tasks.append(task)
        print("tasks added")
        
        
    elif(Choice == 2):
        print("\nyour task")
        for i in range(len(tasks)):
            print(i + 1,".",tasks[i])
            
            
    elif(Choice == 3):
        delete_task = int(input("enter the tasks number to delete: "))
        if(delete_task <= len(tasks)):
            tasks.pop(delete_task -1)
            print("task deleted")

        else:
            print("task does not exist")

            
            
    elif(Choice == 4):
        print("program closed")
        break
    

    else:
        print("invalid choice")
        break