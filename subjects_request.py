import requests

# Source: Open Library 
class SubjectsRequest:

    def __init__(self):
        self.SUBJECT_BASE_URL = 'http://openlibrary.org/subjects/'

    def get_subject_info(self, subject_name, details=False, ebooks=False, published_in=None, limit=1, offset=0):
        url = f"{self.SUBJECT_BASE_URL}{subject_name}.json"

        params = {'details': details, 'ebooks': ebooks, 'published_in': published_in, 'limit': limit, 'offset': offset}
        response = requests.get(url, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch subject information. Status code: {response.status_code}")
            return None