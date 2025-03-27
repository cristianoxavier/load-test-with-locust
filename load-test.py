from locust import TaskSet, task, HttpUser

class ConverterTasks(TaskSet):
    @task
    def hello_world(self):
        self.client.get('/')



class ApiUser(HttpUser):
    task_set = ConverterTasks
    min_wait = 1000
    max_wait = 3000