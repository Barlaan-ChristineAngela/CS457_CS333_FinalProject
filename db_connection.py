import psycopg2

class DatabaseConnection:

    def __init__(self, dbname='CS457_FP', user='postgres', password='092503', host='localhost', port='5432'):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port  
            )
        self.cursor = self.conn.cursor()

    # establish a connection to the database
    def connect(self):
        try:
            self.conn
            print(f"Established connection to {self.dbname}")
            self.cursor
        except psycopg2.Error as error:
            print(f"Could not establish connection to {self.dbname}")
            print(error)
            self.close_connection()
    
    # write SQL queries and fetch statements here
    def insert_user_made_keyword(self, subject_keyword):
        query = '''INSERT INTO Subjects (subject)
                   VALUES (%s)'''
        self.cursor.execute(query, (subject_keyword,))
        self.conn.commit()

    def insert_setting_keyword(self, setting_keyword):
        query = '''INSERT INTO Settings (setting_name)
                   VALUES (%s);'''

        self.cursor.execute(query, (setting_keyword,))
        self.conn.commit()
    
    def insert_character_keyword(self, character_keyword):
        query = '''INSERT INTO Characters (character_name)
                   VALUES (%s);'''

        self.cursor.execute(query, (character_keyword,))
        self.conn.commit()
        
    def insert_genre_keyword(self, genre_keyword):
        query = '''INSERT INTO Genres (genre_name)
                   VALUES (%s);'''

        self.cursor.execute(query, (genre_keyword,))
        self.conn.commit()

    def insert_plot_keyword(self, plot_keyword):
        query = '''INSERT INTO Plots (plot_description)
                   VALUES (%s);'''
        self.cursor.execute(query, (plot_keyword,))
        self.conn.commit()
        
    def insert_description_from_API(self, description):
        query = '''INSERT INTO Stories (description) 
                   VALUES (%s);'''
        self.cursor.execute(query, (description,))
        self.conn.commit()

    def get_settings_table(self):
        query = '''SELECT *
                   FROM Settings;'''
        self.cursor.execute(query)
        settings_table = self.cursor.fetchall()
        return settings_table

    def get_subjects_table(self):
        query = '''SELECT *
                   FROM Subjects;'''
        self.cursor.execute(query)
        subjects_table = self.cursor.fetchall()
        return subjects_table
    
    def get_characters_table(self):
        query = '''SELECT *
                   FROM Characters;'''
        self.cursor.execute(query)
        characters_table = self.cursor.fetchall()
        return characters_table
    
    def get_genres_table(self):
        query = '''SELECT *
                   FROM Genres;'''
        self.cursor.execute(query)
        genres_table = self.cursor.fetchall()
        return genres_table
    
    def get_plots_tables(self):
        query = '''SELECT *
                   FROM Plots;'''
        self.cursor.execute(query)
        plots_table = self.cursor.fetchall()
        return plots_table

    def get_story_descriptions(self):
        query = '''SELECT description
                   FROM Stories;''' 
        self.cursor.execute(query)
        descriptions = self.cursor.fetchall()
        return descriptions
        
    def close_connection(self):
        self.cursor.close()
        self.conn.close()
    
    

