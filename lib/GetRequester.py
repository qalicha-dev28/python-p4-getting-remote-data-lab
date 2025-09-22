import requests

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        # return raw bytes instead of decoded string
        response = requests.get(self.url)
        return response.content  

    def load_json(self):
        # return parsed JSON (Python dict/list)
        response = requests.get(self.url)
        return response.json()
