import requests
import time


class PageController:
    def __init__(self):
        self.current_page = 1

    def increment(self):
        magic_mirror_url = 'http://192.168.50.145:8080/api/notification/PAGE_INCREMENT'
        headers = {'Authorization': 'apiKey 3fab5fbf6c4842b3a3e8c8131cd62820', 'Content-Type': 'application/json'}
        requests.post(magic_mirror_url, headers=headers)
        self.current_page = min(self.current_page + 1, 4)

    def decrement(self):
        magic_mirror_url = 'http://192.168.50.145:8080/api/notification/PAGE_DECREMENT'
        headers = {'Authorization': 'apiKey 3fab5fbf6c4842b3a3e8c8131cd62820', 'Content-Type': 'application/json'}
        requests.post(magic_mirror_url, headers=headers)
        self.current_page = max(self.current_page - 1, 1)

    def change_page(self, target_page):
        while self.current_page < target_page:
            self.increment()
            time.sleep(0.2)
        while self.current_page > target_page:
            self.decrement()
            time.sleep(0.2)
        return self.current_page

if __name__ == "__main__":
    page_controller = PageController()
    page_controller.change_page(3)  # Move to page 3
    print("Current Page:", page_controller.current_page)

