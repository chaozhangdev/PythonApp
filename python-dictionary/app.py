import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word: str) -> str:
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        yn = input("Did you mean %s instead? Enter Y is yes, or N is no: " % get_close_matches(word, data.keys())[0])
        if (yn == "Y") or (yn == "y"):
            return data[get_close_matches(word, data.keys())[0]]
        if (yn == "N") or (yn == "n"):
            return ("The word doesn't exist. Please double check it.")
        else:
            return "Sorry, we can't understand your entry."
    else:
        return ("The word doesn't exist. Please double check it.")

while True: 
    word = input("Enter a word: ") 
    result = translate(word)
    if type(result) == list:
        n = 1
        for item in result:
            print (str(n) + ": " + item)
            n += 1
    else:
        print (result)
    print ("\n")