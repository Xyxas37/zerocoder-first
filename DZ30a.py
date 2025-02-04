import requests
from bs4 import BeautifulSoup
from googletrans import Translator


# Функция для получения английских слов и их определения
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка при получении слова: {e}")
        return None


# Игра на русском языке
def word_game():
    print("Добро пожаловать в игру \"Угадай слово\"!")
    print("Вам будет дано описание английского слова, и вам нужно угадать его перевод на русский.")

    while True:
        # Получаем слово и описание
        word_data = get_english_words()
        if not word_data:
            print("Не удалось получить данные. Попробуйте позже.")
            break

        english_word = word_data.get("english_word")
        word_definition = word_data.get("word_definition")

        # Перевод слова на русский
        translator = Translator()
        try:
            translated_word = translator.translate(english_word, dest="ru").text
        except Exception as e:
            print(f"Ошибка перевода: {e}")
            translated_word = "не удалось перевести"

        # Показываем игроку описание слова
        print(f"\nОписание: {word_definition}")
        user_input = input("Введите перевод слова: ").strip()

        # Проверка ответа
        if user_input.lower() == translated_word.lower():
            print("Верно! Вы угадали слово!")
        else:
            print(f"Неверно. Правильный ответ: {translated_word} ({english_word})")

        # Возможность сыграть ещё раз
        play_again = input("\nХотите сыграть ещё раз? (да/нет): ").strip().lower()
        if play_again != "да":
            print("Спасибо за игру! До встречи!")
            break


# Запуск игры
word_game()

