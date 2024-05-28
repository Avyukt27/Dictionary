import requests
from playsound import playsound
from argparse import ArgumentParser

DICTIONARY: str = "https://api.dictionaryapi.dev/api/v2/entries/en/"

parser = ArgumentParser(
    "Terminal Dictionary",
    "To define words in those times of need",
    "It's a dictionary in your terminal"
)

parser.add_argument("word", type=str, help="The word you want to define")
args = parser.parse_args()
word = vars(args)['word']

def define_word(data: list[dict]) -> None:
    meanings: list[dict] = data[0]["meanings"]
    for meaning in meanings:
        print(f'\nPart of Speech: {meaning['partOfSpeech']}')
        for definition in meaning['definitions']:
            print(f"Meaning: {definition['definition']}")
            print(f"Example: {definition['example']}\n") if 'example' in definition.keys() else None
        print(f"Synonyms: {', '.join(meaning['synonyms'])}") if meaning['synonyms'] else None
        print(f"Antonyms: {', '.join(meaning['antonyms'])}") if meaning['antonyms'] else None

def say_word(data: list[dict]) -> None:
    for dit in data[0]['phonetics']:
        playsound(dit['audio']) if dit['audio'] else None

def main() -> None:
    data: list[dict] = requests.get(DICTIONARY + word).json()
    define_word(data)
    
    hear: str = input("Do you want to hear the word: ")
    if hear.lower() in ['y', 'yes', 'yeah', 'yup']:
        say_word(data)

if __name__ == "__main__":
    main()