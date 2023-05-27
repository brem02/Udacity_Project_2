from locust import HttpUser, task, between

class WebsiteTestUser(HttpUser):
    wait_time = between(0.5, 3.0)

    @task(1)
    def test1(self):
        self.client.get("https://mywebapp20230504.azurewebsites.net")

    @task(2)
    def test2(self):
        self.client.post("https://mywebapp20230504.azurewebsites.net:443/predict")
