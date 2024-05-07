import unittest
from unittest.mock import MagicMock
from user import User

class TestUser(unittest.TestCase):

    def setUp(self):
        self.user = User()

    def test_insert_subject_word(self):
        word = "test"
        self.user.database.insert_user_made_keyword = MagicMock()
        result = self.user.insert_subject_word(word)
        self.assertEqual(result, word)
        self.user.database.insert_user_made_keyword.assert_called_once_with(word)

    def test_incorrectly_inserted_subject_word(self):
        word = "test test"
        with unittest.mock.patch('builtins.print') as mock_print:
            result = self.user.insert_subject_word(word)
            self.assertIsNone(result)
            mock_print.assert_called_once_with("Error: Please enter only one word.")

    def test_view_stories_when_available(self):
        self.user.database.get_story_descriptions = MagicMock(return_value=[("Story 1",), ("Story 2",)])
        with unittest.mock.patch('builtins.print') as mock_print:
            self.user.view_stories()
            mock_print.assert_any_call("Story 1")
            mock_print.assert_any_call("Story 2")

    def test_view_stories_when_not_available(self):
        self.user.database.get_story_descriptions = MagicMock(return_value=[])
        with unittest.mock.patch('builtins.print') as mock_print:
            self.user.view_stories()
            mock_print.assert_called_once_with("No stories available to view.")

if __name__ == "__main__":
    unittest.main()