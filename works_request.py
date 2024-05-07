import requests

# Source: Open Library
class WorksRequest:

    def __init__(self):
        self.WORK_BASE_URL = 'https://openlibrary.org/works/'

    def extract_work_id(self, subject_info):
        work_ids = []
        works = subject_info.get('works', [])
        for work in works:
            work_id = work.get('key', '').replace('/works/', '')
            if work_id:
                work_id = work_id.strip("[]\"")
                work_ids.append(work_id)
        return work_id

    def get_work_description(self, work_id):
        url = f"{self.WORK_BASE_URL}{work_id}.json"
        print(url)
        response = requests.get(url)
        if response.status_code == 200:
            work_info = response.json()
            description = work_info.get('description', '')
            return description
        else:
            print(f"Error: Unable to fetch work information for work ID {work_id}. Status code: {response.status_code}")
            return None