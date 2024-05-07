# import unittest
# from text_processing import TextProcessing

# class TestTextProcessing(unittest.TestCase):

#     def setUp(self):
#         self.process = TextProcessing()

#     def test_process_text(self):
#         text = "This is a test sentence."
#         doc = self.process.process_text(text)
#         self.assertIsNotNone(doc)
#         self.assertEqual(doc.text, text)

#     def test_get_settings(self):
#         text = "The setting is in a small village surrounded by mountains."
#         settings = self.process.get_settings(text)
#         self.assertIn("village", settings)
#         self.assertIn("mountains", settings)

#     def test_get_characters(self):
#         text = "The main characters are Alice and Bob."
#         characters = self.process.get_characters(text)
#         self.assertIn("Alice", characters)
#         self.assertIn("Bob", characters)

#     def test_get_genres(self):
#         text = "This is a science fiction novel."
#         genres = self.process.get_genres(text)
#         self.assertIn("novel", genres)
#         self.assertIn("science", genres)
#         self.assertIn("fiction", genres)

#     def test_get_plots(self):
#         text = "The hero defeats the villain and saves the day."
#         plots = self.process.get_plots(text)
#         self.assertIn("defeats", plots)
#         self.assertIn("saves", plots)

# if __name__ == "__main__":
#     unittest.main()
