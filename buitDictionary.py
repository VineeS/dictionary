import json
from difflib import get_close_matches

def dictionary(word):
    data = json.load(open("/Users/vinee/Downloads/data.json"))
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys())) > 0:
        final = get_close_matches(word,data)[0]
        close_enough = input(f'do you mean "{final}" ? : ')
        if close_enough == "yes":
            return data[final]
        elif close_enough == "no":
            return "The word does not exist please double check it "
        else: 
            return "We did not Understand your input"
    else:
        return "The word is not in the dictionary"

word = input("Enter word : ")
output = dictionary(word)

for i in output:
    print(i)


