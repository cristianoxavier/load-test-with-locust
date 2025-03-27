from locust import task, HttpUser


class ApiUser(HttpUser):
    @task
    def hello_world(self):
        self.client.get('/hello')
    min_wait = 1000
    max_wait = 3000