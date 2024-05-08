import spacy

class TextProcessing:

    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")

    def process_text(self, text):
        doc = self.nlp(text)
        return doc

    def get_settings(self, text):
        doc = self.process_text(text)
        settings = [token.text for token in doc if token.pos_ == "NOUN"]
        return settings

    def get_characters(self, text):
        doc = self.process_text(text)
        characters = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
        return characters

    def get_genres(self, text):
        doc  = self.process_text(text)
        genres = [token.text for token in doc if token.pos_ == "NOUN"]
        return genres 

    def get_plots(self, text):
        doc = self.process_text(text)
        plots = [token.text for token in doc if token.pos_ == "VERB"]
        return plots
