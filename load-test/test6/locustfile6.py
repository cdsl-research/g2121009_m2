from locust import HttpUser, TaskSet, task, constant, FastHttpUser, constant_pacing
from locust import LoadTestShape

class UserTasks(TaskSet):
    @task(3)
    def get_root(self):
        self.client.get("http://192.168.100.38:32604/index.php/")
    @task(2)
    def get_all_courses(self):
        self.client.get("http://192.168.100.38:32604/all-courses/")
    @task(2)
    def get_about(self):
        self.client.get("http://192.168.100.38:32604/about/")
    @task(1)
    def get_contact(self):
        self.client.get("http://192.168.100.38:32604/contact/")

class WebsiteUser(FastHttpUser):
    wait_time = constant_pacing(1)
    tasks = [UserTasks]

class StagesShape(LoadTestShape):
    stages = [{'duration': 60, 'users': 50, 'spawn_rate': 50} ,
{'duration': 120, 'users': 31, 'spawn_rate': 31} ,
{'duration': 180, 'users': 25, 'spawn_rate': 25} ,
{'duration': 240, 'users': 27, 'spawn_rate': 27} ,
{'duration': 300, 'users': 29, 'spawn_rate': 29} ,
{'duration': 360, 'users': 20, 'spawn_rate': 20} ,
{'duration': 420, 'users': 28, 'spawn_rate': 28} ,
{'duration': 480, 'users': 18, 'spawn_rate': 18} ,
{'duration': 540, 'users': 24, 'spawn_rate': 24} ,
{'duration': 600, 'users': 30, 'spawn_rate': 30} ,
{'duration': 660, 'users': 60, 'spawn_rate': 60} ,
{'duration': 720, 'users': 55, 'spawn_rate': 55} ,
{'duration': 780, 'users': 60, 'spawn_rate': 60} ,
{'duration': 840, 'users': 44, 'spawn_rate': 44} ,
{'duration': 900, 'users': 48, 'spawn_rate': 48} ,
{'duration': 960, 'users': 35, 'spawn_rate': 35} ,
{'duration': 1020, 'users': 48, 'spawn_rate': 48} ,
{'duration': 1080, 'users': 45, 'spawn_rate': 45} ,
{'duration': 1140, 'users': 39, 'spawn_rate': 39} ,
{'duration': 1200, 'users': 58, 'spawn_rate': 58} ,
{'duration': 1260, 'users': 56, 'spawn_rate': 56} ,
{'duration': 1320, 'users': 54, 'spawn_rate': 54} ,
{'duration': 1380, 'users': 56, 'spawn_rate': 56} ,
{'duration': 1440, 'users': 62, 'spawn_rate': 62}]
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
        #13:08~13:32