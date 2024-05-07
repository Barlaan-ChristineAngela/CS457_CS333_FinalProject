This program is a simple text analyzer. It uses the OpenLibrary Subjects API and Works API to request subject data. The subject data written in a JSON file is then parsed to retrieve a "key", referred to as a work ID in this program. The work ID is used to retrieve the JSON file for a specific "work" or book. The file contains relevant information such as the author, related subjects, geenres, and a description. The description is parsed to be inserted in the database. The SpaCy library is used to process the description into keywords that are inserted in the database.

The following is an overview of the functionality of the system:

  - Connect to the db 
  - Accept input text for a subject
  - Insert the subject word into the db
  - Use the subject keyword to request to OpenLibrary Subject API for related works
  - Retrieve and parse the descriptions for each subject
  - Process the description for the relevant keywords
  - Insert the processed keywords into the db
  - Insert description into the db
  - Close the db connection

The program uses the following:

  - Installation of psycopg2
  - Installation of SpaCy
  - The SpaCy English trained pipeline for efficiency, en_core_web_sm
  - Python3
  - PostgreSQL
  - Open Library Subjects API and Works API

Note: The outside data source is stored in the "Stories" table as a description retrieved from the API as the user writes subject keywords into the program to be processed. In order for the program to work as expected, the user must enter several keywords to begin with.

To run the program through the terminal, ensure that you are in the working directory of the program. 

Type in

 	python main.py

You will be prompted with 

	$ python main.py
	Established connection to CS457_FP
	Welcome to the Story Keyword Generator!
	This program analyzes text from story summaries.
	Press '1' to write keyword to analyze a random story.
	Press '2' to view a story that was previously analyzed.
	Press '3' to view subjects you previously wrote and that have been processed.




 
