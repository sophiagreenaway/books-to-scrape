import re

#CLEANS FILENAMES
def clean_name(text: str):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "_", text) #FIND EVERY INSTANCE OF CHARACTERS THAT ARE NOT A-Z AND 0-9
    return text.strip("_") #REPLACES EVERYTHING UGLY WITH UNDERSCORES