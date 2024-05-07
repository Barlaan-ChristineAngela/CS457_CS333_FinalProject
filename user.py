from db_connection import DatabaseConnection

class User:

    def __init__(self):
        self.database = DatabaseConnection()

    def insert_subject_word(self, word):
        # accept a subject word from user input
        # insert the subject word in the db (Subjects table)
        if ' ' in word.strip():
            print("Error: Please enter only one word.")
            return None
        
        self.database.insert_user_made_keyword(word)
        return word
    
    def view_stories(self):
        stories = self.database.get_story_descriptions()
        if stories:
            for story in stories:
                print(story[0])
        else:
            print("No stories available to view.")
