from db_connection import DatabaseConnection
from subjects_request import SubjectsRequest
from works_request import WorksRequest
from user import User


def main():
    
    # connect to the database
    database = DatabaseConnection()

    database.connect()

    # output to CLI for user instruction
    print("Welcome to the Story Keyword Generator!")
    print("This program analyzes text from story summaries.")
    # ask the user to make a selection
    user_selection = int(input("Press '1' to write keyword to analyze a random story.\nPress '2' to view a story that was previously analyzed.\nPress '3' to view subjects you previously wrote and that have been processed.\n"))

    user_action = User()
    if user_selection == 1:

        # ask user to write a single word for subject keyword input
        new_keyword = input("Please write a single subject keyword with no spaces.\n")
        user_action.insert_subject_word(new_keyword)

        # request from the Open Library Subjects API for a set of works related to the subject keyword input
        new_subject_request = SubjectsRequest()
        subject_work_info = new_subject_request.get_subject_info(new_keyword)

        # parse the json file from the Subjects API request for the work ID
        # request from the Open Library Works API for the related json of the work
        # parse the work json file for the description
        # insert the description text into the database
        new_works_request = WorksRequest()
        work_id = new_works_request.extract_work_id(subject_work_info)
        work_description = new_works_request.get_work_description(work_id)
        database.insert_description_from_API(work_description)

        # process the text

        setting_keywords = "USA"
        print("Settings:", setting_keywords)

        character_keywords = "Pompompurin"
        print("Characters:", character_keywords)

        genre_keywords = "adventure"
        print("Genres:", genre_keywords)

        plot_keywords = "mystery"
        print("Plots:", plot_keywords)

        # insert the newly processed keywords into the db
        for setting_keyword in setting_keywords:
            database.insert_setting_keyword(setting_keyword)

        for character_keyword in character_keywords:
            database.insert_character_keyword(character_keyword)

        for genre_keyword in genre_keywords:
            database.insert_genre_keyword(genre_keyword)

        for plot_keyword in plot_keywords:
            database.insert_plot_keyword(plot_keyword)

    # retrieve all the descriptions from the db
    elif user_selection == 2:
        stories = user_action.view_stories()
        print(stories)

    # retrieve all the processed keyword tables from the db
    elif user_selection == 3:
        subjects = database.get_subjects_table()
        print("Subject Keywords\n")
        if subjects:
            for subject in subjects:
                print(subject)
        print("\n")

        settings = database.get_settings_table()
        print("Setting Keywords\n")
        if settings:
            for setting in settings:
                print(setting)
        print("\n")

        characters = database.get_characters_table()
        print("Character Keywords\n")
        if characters:
            for character in characters:
                print(character)
        print("\n")

        genres = database.get_genres_table()
        print("Genre Keywords\n")
        if genres:
            for genre in genres:
                print(genre)
        print("\n")

        plots = database.get_plots_tables()
        print("Plot keywords\n")
        if plots:
            for plot in plots:
                print(plot)
        print("\n")

        print(subjects)
        print(settings)
        print(characters)
        print(genres)
        print(plots)

    database.close_connection()

if __name__ == "__main__":
    main()