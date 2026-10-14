import os

file_name="text_file.txt"

def read_task():
    tasks={}
    if os.path.exists(file_name):
        with open(file_name, 'r') as file:
            for keys in file:
                task_id,title,status=keys.strip().split(" | ")
                tasks[int(task_id)]={
                    "title":title,
                    "status":status
                }
    return tasks

def save_task(tasks):
        with open(file_name,'w') as file:
             for task_id,task in tasks.items():
                  file.write(f"{task_id} | {task['title']} | {task['status']} \n")

def add_task(tasks):
     title=input("Enter a task")
     task_id=max(tasks.keys(),default=0) + 1
     tasks[task_id]={"title":title , "status": "incomplete"}
     print(f"task {title} added \b")


def view_task(tasks):
    if not tasks:
        print("no tasks ")
    else:
        for task_id, task in tasks.items():
            print(f"[{task_id}] {task['title']} - {task['status']}")


def mark_comp(tasks):
    task_id=int(input("enter task id to mark as complete"))
    if task_id in tasks:
        tasks[task_id]['status']="complete"
        print("Task mark as completed")
    else:
        print("task not found")


def dele_task(tasks):
    task_id=int(input("enter task id to delete"))
    if task_id in tasks:
        task_del=tasks.pop(task_id)
        print("Task deleted")
    else:
        print("task not found")


def main():
    tasks=read_task()

    while True:
        print("Task menu")
        print("1.add task")
        print("2.View Tasks")
        print("3. mark as complete")
        print("4. delete task")
        print("5. exit")
        choice=input("enter your choice")

        if choice=="1":
            add_task(tasks)
        elif choice=="2":
            view_task(tasks)
        elif choice=="3":
            mark_comp(tasks)
        elif choice=="4":
            dele_task(tasks)
        elif choice=="5":
            save_task(tasks)
            print("Bye")
            break
        else:
            print("try again")

if __name__=="__main__":
    main()