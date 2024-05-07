import unittest
from db_connection import DatabaseConnection

class TestDBConnection(unittest.TestCase):

    def setUp(self):
        self.database = DatabaseConnection()

    def test_connect(self):
        self.assertIsNotNone(self.database.conn)
        self.assertIsNotNone(self.database.cursor)

    def test_insert_user_made_keyword(self):
        keyword = "cats"
        self.database.get_subjects_table()
        self.database.insert_user_made_keyword(keyword)
        updated_subjects = self.database.get_subjects_table()
        self.assertIn((len(updated_subjects), keyword), updated_subjects)

    def test_insert_setting_keyword(self):
        keyword = "France"
        self.database.insert_setting_keyword(keyword)
        self.database.get_settings_table()
        updated_settings = self.database.get_settings_table()
        self.assertIn((len(updated_settings), keyword), updated_settings)

    def test_insert_character_keyword(self):
        keyword = "Pompompurin"
        self.database.insert_character_keyword(keyword)
        self.database.get_characters_table()
        updated_characters = self.database.get_characters_table()
        self.assertIn((len(updated_characters), keyword), updated_characters)

    def test_insert_genre_keyword(self):
        keyword = "comedy"
        self.database.insert_genre_keyword(keyword)
        self.database.get_genres_table()
        updated_genres = self.database.get_genres_table()
        self.assertIn((len(updated_genres), keyword), updated_genres)

    def test_insert_plot_keyword(self):
        keyword = "adventures"
        self.database.get_plots_tables()
        self.database.insert_plot_keyword(keyword)
        updated_plots = self.database.get_plots_tables()
        self.assertIn((len(updated_plots), keyword), updated_plots)

    def test_insert_description_from_API(self):
        description = "Test Description"
        self.database.insert_description_from_API(description)
        descriptions = self.database.get_story_descriptions()
        self.assertIn((description,), descriptions)

    def test_get_settings_table(self):
        settings = self.database.get_settings_table()
        self.assertIsInstance(settings, list)

    def test_get_subjects_table(self):
        subjects = self.database.get_subjects_table()
        self.assertIsInstance(subjects, list)

    def test_get_characters_table(self):
        characters = self.database.get_characters_table()
        self.assertIsInstance(characters, list)
    
    def test_get_genres_table(self):
        genres = self.database.get_genres_table()
        self.assertIsInstance(genres, list)

    def test_get_plots_tables(self):
        plots = self.database.get_plots_tables()
        self.assertIsInstance(plots, list)
        
    def test_get_story_descriptions(self):
        descriptions = self.database.get_story_descriptions()
        self.assertIsInstance(descriptions, list)

if __name__ == "__main__":
    unittest.main()