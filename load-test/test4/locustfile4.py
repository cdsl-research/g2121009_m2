from locust import HttpUser, TaskSet, task, constant, FastHttpUser, constant_pacing
from locust import LoadTestShape

class UserTasks(TaskSet):
    @task(3)
    def get_root(self):
        self.client.get("http://192.168.100.38:31299/index.php/")
    @task(2)
    def get_new_arrivals(self):
        self.client.get("http://192.168.100.38:31299/index.php/new-arrivals/")
    @task(2)
    def get_shop(self):
        self.client.get("http://192.168.100.38:31299/index.php/shop/")
    @task(2)
    def get_shop2(self):
        self.client.get("http://192.168.100.38:31299/index.php/shop/page/2/")
    @task(2)
    def get_collection(self):
        self.client.get("http://192.168.100.38:31299/index.php/collection/")
    @task(1)
    def get_accessrories(self):
        self.client.get("http://192.168.100.38:31299/product-category/accessories/")
    @task(1)
    def get_bottoms(self):
        self.client.get("http://192.168.100.38:31299/product-category/bottoms/")
    @task(1)
    def get_dresses(self):
        self.client.get("http://192.168.100.38:31299/product-category/dresses/")
    @task(1)
    def get_footwear(self):
        self.client.get("http://192.168.100.38:31299/product-category/footwear/")
    @task(1)
    def get_tops(self):
        self.client.get("http://192.168.100.38:31299/product-category/tops/")

class WebsiteUser(FastHttpUser):
    wait_time = constant_pacing(1)
    tasks = [UserTasks]

class StagesShape(LoadTestShape):
    stages = [{'duration': 60, 'users': 26, 'spawn_rate': 26} ,
{'duration': 120, 'users': 21, 'spawn_rate': 21} ,
{'duration': 180, 'users': 13, 'spawn_rate': 13} ,
{'duration': 240, 'users': 8, 'spawn_rate': 8} ,
{'duration': 300, 'users': 6, 'spawn_rate': 6} ,
{'duration': 360, 'users': 15, 'spawn_rate': 15} ,
{'duration': 420, 'users': 10, 'spawn_rate': 10} ,
{'duration': 480, 'users': 12, 'spawn_rate': 12} ,
{'duration': 540, 'users': 29, 'spawn_rate': 29} ,
{'duration': 600, 'users': 53, 'spawn_rate': 53} ,
{'duration': 660, 'users': 78, 'spawn_rate': 78} ,
{'duration': 720, 'users': 83, 'spawn_rate': 83} ,
{'duration': 780, 'users': 59, 'spawn_rate': 59} ,
{'duration': 840, 'users': 63, 'spawn_rate': 63} ,
{'duration': 900, 'users': 71, 'spawn_rate': 71} ,
{'duration': 960, 'users': 57, 'spawn_rate': 57} ,
{'duration': 1020, 'users': 52, 'spawn_rate': 52} ,
{'duration': 1080, 'users': 60, 'spawn_rate': 60} ,
{'duration': 1140, 'users': 41, 'spawn_rate': 41} ,
{'duration': 1200, 'users': 41, 'spawn_rate': 41} ,
{'duration': 1260, 'users': 34, 'spawn_rate': 34} ,
{'duration': 1320, 'users': 54, 'spawn_rate': 54} ,
{'duration': 1380, 'users': 53, 'spawn_rate': 53} ,
{'duration': 1440, 'users': 60, 'spawn_rate': 60} ]
    def tick(self):
        run_time = self.get_run_time()
        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data
        return None
        #13:08~13:32