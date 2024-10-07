from tkinter import *

# Function to add a task to the listbox
def add_task():
    task = task_entry.get()
    if task != "":
        task_list.insert(END, task)
        task_entry.delete(0, END)

# Function to delete a task from the listbox
def delete_task():
    selected_task_index = task_list.curselection()
    task_list.delete(0, selected_task_index)

# Function to clear all tasks from the listbox
def clear_tasks():
    task_list.delete(0, END)

# Main window setup
root = Tk()
root.title("To-Do List")
root.geometry("400x400")

# Widgets
task_entry = Entry(root, width=40)
task_entry.pack()

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack()

delete_button = Button(root, text="Delete Task", command=delete_task)
delete_button.pack()

clear_button = Button(root, text="Clear Tasks", command=clear_tasks)
clear_button.pack()

task_list = Listbox(root, width=50, height=15)
task_list.pack()

if __name__ == '__main__':
	mainloop()
