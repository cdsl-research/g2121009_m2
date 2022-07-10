from locust import HttpUser, TaskSet, task, constant, FastHttpUser, constant_pacing
from locust import LoadTestShape

class UserTasks(TaskSet):
    @task(3)
    def get_root(self):
        self.client.get("http://192.168.100.38:31802/")
    @task(2)
    def get_about(self):
        self.client.get("http://192.168.100.38:31802/?page_id=129")
    @task(2)
    def get_service(self):
        self.client.get("http://192.168.100.38:31802/?page_id=131")
    @task(2)
    def get_projects(self):
        self.client.get("http://192.168.100.38:31802/?page_id=130")
    @task(2)
    def get_contact(self):
        self.client.get("http://192.168.100.38:31802/?page_id=132")

class WebsiteUser(FastHttpUser):
    wait_time = constant_pacing(1)
    tasks = [UserTasks]

class StagesShape(LoadTestShape):
    stages = [{'duration': 60, 'users': 34, 'spawn_rate': 34} ,
{'duration': 120, 'users': 24, 'spawn_rate': 24} ,
{'duration': 180, 'users': 14, 'spawn_rate': 14} ,
{'duration': 240, 'users': 20, 'spawn_rate': 20} ,
{'duration': 300, 'users': 9, 'spawn_rate': 9} ,
{'duration': 360, 'users': 22, 'spawn_rate': 22} ,
{'duration': 420, 'users': 15, 'spawn_rate': 15} ,
{'duration': 480, 'users': 22, 'spawn_rate': 22} ,
{'duration': 540, 'users': 24, 'spawn_rate': 24} ,
{'duration': 600, 'users': 64, 'spawn_rate': 64} ,
{'duration': 660, 'users': 72, 'spawn_rate': 72} ,
{'duration': 720, 'users': 49, 'spawn_rate': 49} ,
{'duration': 780, 'users': 39, 'spawn_rate': 39} ,
{'duration': 840, 'users': 76, 'spawn_rate': 76} ,
{'duration': 900, 'users': 56, 'spawn_rate': 56} ,
{'duration': 960, 'users': 81, 'spawn_rate': 81} ,
{'duration': 1020, 'users': 69, 'spawn_rate': 69} ,
{'duration': 1080, 'users': 76, 'spawn_rate': 76} ,
{'duration': 1140, 'users': 45, 'spawn_rate': 45} ,
{'duration': 1200, 'users': 41, 'spawn_rate': 41} ,
{'duration': 1260, 'users': 29, 'spawn_rate': 29} ,
{'duration': 1320, 'users': 43, 'spawn_rate': 43} ,
{'duration': 1380, 'users': 44, 'spawn_rate': 44} ,
{'duration': 1440, 'users': 31, 'spawn_rate': 31} ]
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
        #13:08~13:32