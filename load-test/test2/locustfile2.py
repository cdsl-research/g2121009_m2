from locust import HttpUser, TaskSet, task, constant, FastHttpUser, constant_pacing
from locust import LoadTestShape

class UserTasks(TaskSet):
    @task(3)
    def get_root(self):
        self.client.get("http://192.168.100.38:32298/")
    @task(2)
    def get_plants(self):
        self.client.get("http://192.168.100.38:32298/?post_type=product")
    @task(2)
    def get_plants2(self):
        self.client.get("http://192.168.100.38:32298/?post_type=product&paged=2")
    @task(2)
    def get_plants3(self):
        self.client.get("http://192.168.100.38:32298/?post_type=product&paged=3")
    @task(2)
    def get_about(self):
        self.client.get("http://192.168.100.38:32298/?page_id=1002")
    @task(1)
    def get_contact(self):
        self.client.get("http://192.168.100.38:32298/?page_id=1004")

class WebsiteUser(FastHttpUser):
    wait_time = constant_pacing(1)
    tasks = [UserTasks]

class StagesShape(LoadTestShape):
    stages = [{'duration': 60, 'users': 24, 'spawn_rate': 24} ,
{'duration': 120, 'users': 28, 'spawn_rate': 28} ,
{'duration': 180, 'users': 14, 'spawn_rate': 14} ,
{'duration': 240, 'users': 11, 'spawn_rate': 11} ,
{'duration': 300, 'users': 8, 'spawn_rate': 8} ,
{'duration': 360, 'users': 9, 'spawn_rate': 9} ,
{'duration': 420, 'users': 9, 'spawn_rate': 9} ,
{'duration': 480, 'users': 16, 'spawn_rate': 16} ,
{'duration': 540, 'users': 31, 'spawn_rate': 31} ,
{'duration': 600, 'users': 65, 'spawn_rate': 65} ,
{'duration': 660, 'users': 58, 'spawn_rate': 58} ,
{'duration': 720, 'users': 65, 'spawn_rate': 65} ,
{'duration': 780, 'users': 71, 'spawn_rate': 71} ,
{'duration': 840, 'users': 67, 'spawn_rate': 67} ,
{'duration': 900, 'users': 88, 'spawn_rate': 88} ,
{'duration': 960, 'users': 76, 'spawn_rate': 76} ,
{'duration': 1020, 'users': 57, 'spawn_rate': 57} ,
{'duration': 1080, 'users': 59, 'spawn_rate': 59} ,
{'duration': 1140, 'users': 43, 'spawn_rate': 43} ,
{'duration': 1200, 'users': 39, 'spawn_rate': 39} ,
{'duration': 1260, 'users': 36, 'spawn_rate': 36} ,
{'duration': 1320, 'users': 49, 'spawn_rate': 49} ,
{'duration': 1380, 'users': 40, 'spawn_rate': 40} ,
{'duration': 1440, 'users': 38, 'spawn_rate': 38} ]
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
        #13:08~13:32