Task = []

name = input("What's your name? ")

while True:
    print("What do you want to do ")
    print('1: Create new task')
    print('2: Delete a task')
    print('3: Show all tasks')
    print('4: Exit')

    choice = input('Input your choice: ')
    
    

    if int(choice) == 1:
       new_task = input('Enter the new task :')
       Task.append(new_task)
       print(new_task,'Has been added')
       break

    elif int(choice) == 2:
       delete_task = input('Which task would you like to delete: ')
       if delete_task in Task:
           Task.remove(delete_task)
           break
       else:
           print('Invalid Input.Please Try Again')
    
    elif int(choice) == 3:
        input(Task)
    
    elif int(choice) == 4:

        print('Goodbye,',name)
        break