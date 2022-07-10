from locust import HttpUser, TaskSet, task, constant, FastHttpUser, constant_pacing
from locust import LoadTestShape

class UserTasks(TaskSet):
    @task(3)
    def get_root(self):
        self.client.get("http://192.168.100.38:31128/index.php/")
    @task(2)
    def get_about(self):
        self.client.get("http://192.168.100.38:31128/index.php/about/")
    @task(2)
    def get_menu(self):
        self.client.get("http://192.168.100.38:31128/index.php/menu/")
    @task(1)
    def get_reviews(self):
        self.client.get("http://192.168.100.38:31128/index.php/reviews/")
    @task(1)
    def get_contact(self):
        self.client.get("http://192.168.100.38:31128/index.php/contact/")

class WebsiteUser(FastHttpUser):
    wait_time = constant_pacing(1)
    tasks = [UserTasks]

class StagesShape(LoadTestShape):
    stages = [{'duration': 60, 'users': 27, 'spawn_rate': 27} ,
{'duration': 120, 'users': 22, 'spawn_rate': 22} ,
{'duration': 180, 'users': 35, 'spawn_rate': 35} ,
{'duration': 240, 'users': 11, 'spawn_rate': 11} ,
{'duration': 300, 'users': 17, 'spawn_rate': 17} ,
{'duration': 360, 'users': 11, 'spawn_rate': 11} ,
{'duration': 420, 'users': 11, 'spawn_rate': 11} ,
{'duration': 480, 'users': 14, 'spawn_rate': 14} ,
{'duration': 540, 'users': 15, 'spawn_rate': 15} ,
{'duration': 600, 'users': 47, 'spawn_rate': 47} ,
{'duration': 660, 'users': 61, 'spawn_rate': 61} ,
{'duration': 720, 'users': 68, 'spawn_rate': 68} ,
{'duration': 780, 'users': 80, 'spawn_rate': 80} ,
{'duration': 840, 'users': 57, 'spawn_rate': 57} ,
{'duration': 900, 'users': 87, 'spawn_rate': 87} ,
{'duration': 960, 'users': 57, 'spawn_rate': 57} ,
{'duration': 1020, 'users': 69, 'spawn_rate': 69} ,
{'duration': 1080, 'users': 66, 'spawn_rate': 66} ,
{'duration': 1140, 'users': 38, 'spawn_rate': 38} ,
{'duration': 1200, 'users': 40, 'spawn_rate': 40} ,
{'duration': 1260, 'users': 30, 'spawn_rate': 30} ,
{'duration': 1320, 'users': 38, 'spawn_rate': 38} ,
{'duration': 1380, 'users': 53, 'spawn_rate': 53} ,
{'duration': 1440, 'users': 46, 'spawn_rate': 46} ]
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
        #13:08~13:32