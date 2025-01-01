import unittest

# 被测试的任务管理系统
tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added."

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        return f"Task '{task}' removed."
    else:
        return "Task not found."

def list_tasks():
    return tasks

class TestTaskManager(unittest.TestCase):

    def setUp(self):
        # 每个测试前清空任务列表
        global tasks
        tasks = []

    def test_add_single_task(self):
        result = add_task("Buy groceries")
        self.assertIn("Buy groceries", tasks)
        self.assertEqual(result, "Task 'Buy groceries' added.")

    def test_add_multiple_tasks(self):
        add_task("Buy groceries")
        add_task("Read a book")
        self.assertEqual(len(tasks), 2)
        self.assertIn("Read a book", tasks)

    def test_add_empty_task(self):
        result = add_task("")
        self.assertIn("", tasks)
        self.assertEqual(result, "Task '' added.")

    def test_add_non_string_task(self):
        result = add_task(123)
        self.assertIn(123, tasks)
        self.assertEqual(result, "Task '123' added.")

    def test_remove_existing_task(self):
        add_task("Buy groceries")
        result = remove_task("Buy groceries")
        self.assertNotIn("Buy groceries", tasks)
        self.assertEqual(result, "Task 'Buy groceries' removed.")

    def test_remove_non_existing_task(self):
        add_task("Buy groceries")
        result = remove_task("Read a book")
        self.assertEqual(result, "Task not found.")
        self.assertIn("Buy groceries", tasks)

    def test_remove_empty_task(self):
        add_task("")
        result = remove_task("")
        self.assertNotIn("", tasks)
        self.assertEqual(result, "Task '' removed.")

    def test_remove_non_string_task(self):
        add_task(123)
        result = remove_task(123)
        self.assertNotIn(123, tasks)
        self.assertEqual(result, "Task '123' removed.")

    def test_remove_task_twice(self):
        add_task("Buy groceries")
        remove_task("Buy groceries")
        result = remove_task("Buy groceries")
        self.assertEqual(result, "Task not found.")

    def test_list_tasks_empty(self):
        self.assertEqual(list_tasks(), [])

    def test_list_tasks_with_items(self):
        add_task("Buy groceries")
        add_task("Read a book")
        self.assertEqual(list_tasks(), ["Buy groceries", "Read a book"])

    def test_add_duplicate_tasks(self):
        add_task("Buy groceries")
        add_task("Buy groceries")
        self.assertEqual(tasks.count("Buy groceries"), 2)

    def test_add_task_with_special_characters(self):
        result = add_task("Plan vacation @ 2025!")
        self.assertIn("Plan vacation @ 2025!", tasks)
        self.assertEqual(result, "Task 'Plan vacation @ 2025!' added.")

    def test_add_task_with_whitespace(self):
        result = add_task("   ")
        self.assertIn("   ", tasks)
        self.assertEqual(result, "Task '   ' added.")

if __name__ == '__main__':
    unittest.main()
