from todo import add_task, list_tasks, remove_task

def test_add_and_remove():
    add_task("Test task")
    with open("todo.txt") as f:
        tasks = f.read().splitlines()
    assert "Test task" in tasks
    remove_task(len(tasks))

