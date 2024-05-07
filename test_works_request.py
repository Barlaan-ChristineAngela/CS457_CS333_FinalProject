import unittest
from unittest.mock import MagicMock
from works_request import WorksRequest

class TestWorksRequest(unittest.TestCase):

    def setUp(self):
        self.work = WorksRequest()

    def test_extract_work_id(self):
        subject_info = {'works': [{'key': '/works/OL1W'}]}
        work_id = self.work.extract_work_id(subject_info)
        self.assertEqual(work_id, 'OL1W')

    def test_get_work_description_when_valid_url(self):
        work_id = "OL45804W" # valid key from Open Library
        expected_description = self.work.get_work_description(work_id)
        self.work.WORK_BASE_URL = "https://openlibrary.org/works/"
        description = self.work.get_work_description(work_id)
        self.assertEqual(description, expected_description)

    def test_get_work_description_when_invalid_url(self):
        work_id = "OL1W"
        self.work.WORK_BASE_URL = "https://openlibrary.org/works/"
        expected_description = self.work.get_work_description(work_id)
        self.assertFalse(expected_description)

if __name__ == "__main__":
    unittest.main()
