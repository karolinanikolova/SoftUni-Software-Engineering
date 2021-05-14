# 2.	Todo List
# You will receive a todo-notes until you get the command "End".
# The notes will be in the format: "{importance}-{value}". Return the list of todo-notes sorted by importance.
# The maximum importance will be 10

note = input()

todo_list = [0] * 10

while not note == 'End':
    importance, task = note.split('-')
    # remove one in order for the importance to match the index of the list
    importance = int(importance) - 1
    todo_list[importance] = task

    note = input()

print([task for task in todo_list if not task == 0])

