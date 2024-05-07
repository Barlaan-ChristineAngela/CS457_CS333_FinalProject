import unittest
from unittest.mock import patch, MagicMock
from subjects_request import SubjectsRequest

class TestSubjectsRequest(unittest.TestCase):

    def setUp(self):
        self.subject = SubjectsRequest()
        
    @patch('subjects_request.requests.get')
    def test_get_subject_info_successfully(self, mock_get):
        # Mocking the response
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"subject_name": "Test Subject"}
        mock_get.return_value = mock_response

        subject_info = self.subject.get_subject_info("test_subject")

        self.assertIsNotNone(subject_info)
        self.assertEqual(subject_info["subject_name"], "Test Subject")

    @patch('subjects_request.requests.get')
    def test_get_subject_info_unsuccessfully(self, mock_get):
        # Mocking the response for an unsuccessful request
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_get.return_value = mock_response

        subject_info = self.subject.get_subject_info("non_existing_subject")

        self.assertIsNone(subject_info)
        # Ensure appropriate error message is printed
        self.assertTrue(mock_get.called)
        self.assertTrue("Error: Unable to fetch subject information. Status code: 404")

if __name__ == "__main__":
    unittest.main()
     