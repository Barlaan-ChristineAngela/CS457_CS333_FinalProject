CREATE TABLE Subjects(
	subject_id SERIAL PRIMARY KEY,
	subject VARCHAR(256)
);

CREATE TABLE Settings(
	setting_id SERIAL PRIMARY KEY,
	setting_name VARCHAR(500)
);

CREATE TABLE Characters(
	character_id SERIAL PRIMARY KEY,
	character_name VARCHAR(500)
);

CREATE TABLE Genres(
	genre_id SERIAL PRIMARY KEY,
	genre_name VARCHAR(256)
)

CREATE TABLE Plots(
	plot_id SERIAL PRIMARY KEY,
	plot_description varchar(500)
);

CREATE TABLE Stories(
	story_id SERIAL PRIMARY KEY,
	description TEXT,
	genre_id INT REFERENCES Genres(genre_id),
	setting_id INT REFERENCES Settings(setting_id),
	main_characters INT REFERENCES Characters(character_id),
	plot_id INT REFERENCES Plots(plot_id)
);