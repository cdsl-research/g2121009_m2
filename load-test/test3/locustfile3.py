from locust import HttpUser, TaskSet, task, constant, FastHttpUser, constant_pacing
from locust import LoadTestShape

class UserTasks(TaskSet):
    @task(3)
    def get_root(self):
        self.client.get("http://192.168.100.38:32674/index.php/")
    @task(2)
    def get_about(self):
        self.client.get("http://192.168.100.38:32674/index.php/about/")
    @task(2)
    def get_shop(self):
        self.client.get("http://192.168.100.38:32674/index.php/shop/")
    @task(2)
    def get_shop2(self):
        self.client.get("http://192.168.100.38:32674/index.php/shop/page/2/")
    @task(1)
    def get_contact(self):
        self.client.get("http://192.168.100.38:32674/index.php/contact/")
    @task(1)
    def get_myaccount(self):
        self.client.get("http://192.168.100.38:32674/index.php/my-account/")

class WebsiteUser(FastHttpUser):
    wait_time = constant_pacing(1)
    tasks = [UserTasks]

class StagesShape(LoadTestShape):
    stages = [{'duration': 60, 'users': 25, 'spawn_rate': 25} ,
{'duration': 120, 'users': 29, 'spawn_rate': 29} ,
{'duration': 180, 'users': 11, 'spawn_rate': 11} ,
{'duration': 240, 'users': 16, 'spawn_rate': 16} ,
{'duration': 300, 'users': 10, 'spawn_rate': 10} ,
{'duration': 360, 'users': 6, 'spawn_rate': 6} ,
{'duration': 420, 'users': 9, 'spawn_rate': 9} ,
{'duration': 480, 'users': 19, 'spawn_rate': 19} ,
{'duration': 540, 'users': 41, 'spawn_rate': 41} ,
{'duration': 600, 'users': 32, 'spawn_rate': 32} ,
{'duration': 660, 'users': 67, 'spawn_rate': 67} ,
{'duration': 720, 'users': 60, 'spawn_rate': 60} ,
{'duration': 780, 'users': 64, 'spawn_rate': 64} ,
{'duration': 840, 'users': 50, 'spawn_rate': 50} ,
{'duration': 900, 'users': 66, 'spawn_rate': 66} ,
{'duration': 960, 'users': 71, 'spawn_rate': 71} ,
{'duration': 1020, 'users': 77, 'spawn_rate': 77} ,
{'duration': 1080, 'users': 54, 'spawn_rate': 54} ,
{'duration': 1140, 'users': 50, 'spawn_rate': 50} ,
{'duration': 1200, 'users': 46, 'spawn_rate': 46} ,
{'duration': 1260, 'users': 51, 'spawn_rate': 51} ,
{'duration': 1320, 'users': 57, 'spawn_rate': 57} ,
{'duration': 1380, 'users': 50, 'spawn_rate': 50} ,
{'duration': 1440, 'users': 39, 'spawn_rate': 39} ]
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
        #13:08~13:32