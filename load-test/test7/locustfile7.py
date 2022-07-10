from locust import HttpUser, TaskSet, task, constant, FastHttpUser, constant_pacing
from locust import LoadTestShape

class UserTasks(TaskSet):
    @task(3)
    def get_root(self):
        self.client.get("http://192.168.100.38:32710/")
    @task(2)
    def get_store(self):
        self.client.get("http://192.168.100.38:32710/?post_type=product")
    @task(2)
    def get_store2(self):
        self.client.get("http://192.168.100.38:32710/?post_type=product&paged=2")
    @task(2)
    def get_store3(self):
        self.client.get("http://192.168.100.38:32710/?post_type=product&paged=3")
    @task(2)
    def get_men1(self):
        self.client.get("http://192.168.100.38:32710/?product_cat=men")
    @task(2)
    def get_men2(self):
        self.client.get("http://192.168.100.38:32710/?product_cat=men&paged=2")
    @task(2)
    def get_women1(self):
        self.client.get("http://192.168.100.38:32710/?product_cat=women")
    @task(2)
    def get_women2(self):
        self.client.get("http://192.168.100.38:32710/?product_cat=women&paged=2")
    @task(2)
    def get_accessories(self):
        self.client.get("http://192.168.100.38:32710/?product_cat=accessories")
    @task(1)
    def get_about(self):
        self.client.get("http://192.168.100.38:32710/?page_id=59")
    @task(1)
    def get_contact(self):
        self.client.get("http://192.168.100.38:32710/?page_id=60")

class WebsiteUser(FastHttpUser):
    wait_time = constant_pacing(1)
    tasks = [UserTasks]

class StagesShape(LoadTestShape):
    stages = [{'duration': 60, 'users': 54, 'spawn_rate': 54} ,
{'duration': 120, 'users': 24, 'spawn_rate': 24} ,
{'duration': 180, 'users': 28, 'spawn_rate': 28} ,
{'duration': 240, 'users': 24, 'spawn_rate': 24} ,
{'duration': 300, 'users': 12, 'spawn_rate': 12} ,
{'duration': 360, 'users': 16, 'spawn_rate': 16} ,
{'duration': 420, 'users': 17, 'spawn_rate': 17} ,
{'duration': 480, 'users': 23, 'spawn_rate': 23} ,
{'duration': 540, 'users': 53, 'spawn_rate': 53} ,
{'duration': 600, 'users': 25, 'spawn_rate': 25} ,
{'duration': 660, 'users': 45, 'spawn_rate': 45} ,
{'duration': 720, 'users': 53, 'spawn_rate': 53} ,
{'duration': 780, 'users': 53, 'spawn_rate': 53} ,
{'duration': 840, 'users': 49, 'spawn_rate': 49} ,
{'duration': 900, 'users': 43, 'spawn_rate': 43} ,
{'duration': 960, 'users': 53, 'spawn_rate': 53} ,
{'duration': 1020, 'users': 84, 'spawn_rate': 84} ,
{'duration': 1080, 'users': 51, 'spawn_rate': 51} ,
{'duration': 1140, 'users': 33, 'spawn_rate': 33} ,
{'duration': 1200, 'users': 36, 'spawn_rate': 36} ,
{'duration': 1260, 'users': 48, 'spawn_rate': 48} ,
{'duration': 1320, 'users': 60, 'spawn_rate': 60} ,
{'duration': 1380, 'users': 53, 'spawn_rate': 53} ,
{'duration': 1440, 'users': 63, 'spawn_rate': 63} ]
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
        #13:08~13:32