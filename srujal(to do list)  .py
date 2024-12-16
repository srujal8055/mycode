import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["todo_list"]  # Create a database named "todo_list"
tasks = db["tasks"]  # Create a collection named "tasks" within the database

# Function to display all tasks
def show_tasks():
    print("**Current Tasks**")
    for task in tasks.find():
        status = "COMPLETED" if task['completed'] else "PENDING"
        print("{task['_id']}. {task['task']} ({status})")

# Function to add a new task
def add_task():
    task_desc = input("Enter task description: ")
    tasks.insert_one({"task": task_desc, "completed": False})
    print("Task added successfully!")

# Function to mark a task as completed


# Main loop for user interaction
while True:
    print("\n**To-Do List**")
    print("1. Show Tasks")
    print("2. Add Task")
    
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == 1:
        show_tasks()
    elif choice == 2:
        add_task()
    
    elif choice == 4:
        break
    else:
        print("Invalid choice!")

# Close connection
client.close()
