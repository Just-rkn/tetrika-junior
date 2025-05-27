import requests
import csv
from collections import Counter


WIKI_API_URL = "https://ru.wikipedia.org/w/api.php"
MAX_CM_LIMIT = 500
RUSSIAN_ALPHABET = set('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
MAX_LATIN_STREAK = 10


def get_category_members(
        category: str,
        cmcontinue: str | None = None
) -> tuple[list[dict], str | None]:

    params = {
        'action': 'query',
        'list': 'categorymembers',
        'cmtitle': category,
        'cmlimit': MAX_CM_LIMIT,
        'format': 'json',
        'cmcontinue': cmcontinue
    }

    response = requests.get(WIKI_API_URL, params=params)
    data = response.json()

    members = data['query']['categorymembers']
    cmcontinue = data.get('continue', {}).get('cmcontinue')
    return members, cmcontinue


def count_by_letter(category: str) -> dict:
    counter = Counter()
    cmcontinue = None

    while True:
        latin_streak = 0
        members, cmcontinue = get_category_members(category, cmcontinue)

        for member in members:
            first_letter = member['title'][0].upper()

            if first_letter in RUSSIAN_ALPHABET:
                counter[first_letter] += 1
            else:
                latin_streak += 1

            if latin_streak >= 10 or cmcontinue is None:
                return dict(counter)


def save_to_csv(counter: dict, filename: str):
    with open(filename, 'w', encoding='utf-8', newline='') as f:
        writter = csv.writer(f)
        for letter in sorted(counter.keys()):
            writter.writerow([letter, counter[letter]])


if __name__ == "__main__":
    category = 'Категория:Животные по алфавиту'
    result = count_by_letter(category=category)
    save_to_csv(result, 'result.csv')
