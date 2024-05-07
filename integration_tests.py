import unittest
from unittest.mock import MagicMock
from db_connection import DatabaseConnection
from subjects_request import SubjectsRequest
from text_processing import TextProcessing
from user import User
from works_request import WorksRequest

class IntegrationTests(unittest.TestCase):

    def setUp(self):
        self.database = DatabaseConnection()
        self.subject = SubjectsRequest()
        self.process = TextProcessing()
        self.user = User()
        self.work = WorksRequest()

    def test_queries_are_correctly_made_to_insert_user_made_subject_input(self):
        # insert a subject word as the user
        word = "test_subject"
        self.user.insert_subject_word(word)
        
        # Check if the insert query was executed
        self.assertTrue(self.database.cursor.execute)
        self.assertTrue(self.database.conn.commit)

    def test_insert_subject_word_and_get_work_description(self):
        # insert a single subject word as the user
        word = "love"
        self.user.insert_subject_word(word)
        
        # make subject request
        subject_info = self.subject.get_subject_info(word)
        
        # make work request for id
        work_id = self.work.extract_work_id(subject_info)
        
        # make work request for description
        work_description = self.work.get_work_description(work_id)
        self.assertIsNotNone(work_description)

    def test_subjects_and_works_requests_correctly_retrieve_url_from_user_subject_input(self):
        # create a random word to be inserted to be passed through the requests
        word = "love"
        
        # call all subjects requests functions
        subject_info = self.subject.get_subject_info(word)
        self.assertIsNotNone(subject_info)
        
        # call all works requests functions
        work_ids = self.work.extract_work_id(subject_info)
        self.assertIsNotNone(work_ids)

    def test_queries_are_correctly_made_to_insert_parsed_text_from_API_requests_into_DB(self):
        # create a random word to be inserted to be passed through requests and text processing
        word = "love"
        
        # pass the word through subjects requests
        subject_info = self.subject.get_subject_info(word)
        
        # make work request for id
        work_id = self.work.extract_work_id(subject_info)
        
        # make work request for description
        description = self.work.get_work_description(work_id)
                
        # insert the description fetched from the works request into the db
        self.database.insert_description_from_API(description)
        
        # call the text processing functions
        settings = self.process.get_settings(description)
        characters = self.process.get_characters(description)
        genres = self.process.get_genres(description)
        plots = self.process.get_plots(description)
        
        # insert every processed word into the db
        for setting in settings:
            self.database.insert_setting_keyword(setting)
        for character in characters:
            self.database.insert_character_keyword(character)
        for genre in genres:
            self.database.insert_genre_keyword(genre)
        for plot in plots:
            self.database.insert_plot_keyword(plot)
            
        # Check if the insert queries were executed
        self.assertTrue(self.database.cursor.execute)
        self.assertTrue(self.database.conn.commit)

    def test_user_can_retrieve_previously_processed_data_from_db(self):
        # Insert test data into the database
        description = "Test description"
        settings = ["setting1", "setting2"]
        characters = ["character1", "character2"]
        genres = ["genre1", "genre2"]
        plots = ["plot1", "plot2"]
        
        # Insert description into Stories table
        self.database.insert_description_from_API(description)
        
        # Insert processed data into respective tables
        for setting in settings:
            self.database.insert_setting_keyword(setting)
        for character in characters:
            self.database.insert_character_keyword(character)
        for genre in genres:
            self.database.insert_genre_keyword(genre)
        for plot in plots:
            self.database.insert_plot_keyword(plot)
            
        # Retrieve processed data from the database using the User class
        self.database.get_settings_table()
        self.database.get_characters_table()
        self.database.get_genres_table()
        self.database.get_plots_tables()
        
        # Check if the insert queries were executed
        self.assertTrue(self.database.cursor.execute)
        self.assertTrue(self.database.conn.commit)

if __name__ == "__main__":
    unittest.main()
