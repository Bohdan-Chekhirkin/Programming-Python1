import json
import os

# Функція для перевірки парності або закінчення на 7
def is_even_or_ends_with_7(number):
    return number % 2 == 0 or str(number).endswith('7')

# Функція для перекладу тексту (приклад)
def translate(key, language):
    translations = {
        "enter_numbers": {
            "en": "Please enter two integers (a and b): ",
            "uk": "Будь ласка, введіть два цілих числа (a та b): "
        },
        "select_language": {
            "en": "Choose language (en/uk): ",
            "uk": "Виберіть мову (en/uk): "
        },
        "file_not_found": {
            "en": "Data file is missing or corrupted.",
            "uk": "Файл з даними відсутній або некоректний."
        },
        "data_saved": {
            "en": "Data saved. Program terminated.",
            "uk": "Дані збережено. Програма завершена."
        },
        "result_even": {
            "en": "The absolute sum |a + b| is even or ends with 7.",
            "uk": "Абсолютна сума |a + b| є парною або закінчується на 7."
        },
        "result_odd": {
            "en": "The absolute sum |a + b| is neither even nor ends with 7.",
            "uk": "Абсолютна сума |a + b| не є парною і не закінчується на 7."
        }
    }
    return translations[key].get(language, translations[key]["uk"])  # За замовчуванням українська

def main():
    # Шлях до файлу
    filename = "MyData.txt"
    
    # Спроба прочитати файл
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            try:
                data = json.load(file)
                a = data.get("a")
                b = data.get("b")
                language = data.get("language", "uk")
                if a is None or b is None:
                    raise ValueError("Missing data")
            except (json.JSONDecodeError, ValueError) as e:
                print(translate("file_not_found", "uk"))
                a, b, language = get_user_input()
    else:
        print(translate("file_not_found", "uk"))
        a, b, language = get_user_input()
    
    # Обробка введених даних
    a = abs(a)  # Зміна знаку на позитивний, якщо a від'ємне
    b = abs(b)  # Зміна знаку на позитивний, якщо b від'ємне

    absolute_sum = abs(a + b)

    # Перевірка умов
    if is_even_or_ends_with_7(absolute_sum):
        print(translate("result_even", language))
    else:
        print(translate("result_odd", language))

def get_user_input():
    # Введення користувача
    numbers = input(translate("enter_numbers", "uk"))
    a, b = map(int, numbers.replace(',', ' ').split())  # Заміна коми на пробіл
    language = input(translate("select_language", "uk"))
    
    # Збереження даних у файл
    with open("MyData.txt", 'w') as file:
        json.dump({"a": a, "b": b, "language": language}, file)
    
    print(translate("data_saved", language))
    return a, b, language

if __name__ == "__main__":
    main()