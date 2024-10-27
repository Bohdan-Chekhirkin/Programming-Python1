import re

def custom_sort(word):
    """Функція для сортування слів за українським та англійським алфавітом."""
    return (word.lower(), word)

def get_input_text():
    """Функція для отримання тексту від користувача."""
    print("Будь ласка, введіть текст:")
    input_text = input()  # Зчитуємо текст з консолі
    return input_text

def sort_words(text):
    """Функція для виділення, очищення та сортування слів."""
    # Знайти всі слова, очистити від знаків пунктуації
    words = re.findall(r'\b\w+\b', text)
    
    # Сформувати списки українських і англійських слів
    ukrainian_words = [word for word in words if re.search(r'[А-ЩЬЮЯа-щьюяїієґ]', word)]
    english_words = [word for word in words if re.search(r'[A-Za-z]', word)]
    
    # Сортування слів
    ukrainian_words.sort(key=custom_sort)
    english_words.sort(key=custom_sort)
    
    # Об'єднати два списки
    sorted_words = ukrainian_words + english_words
    return sorted_words

def main():
    input_text = get_input_text()  # Отримуємо текст від користувача
    if input_text:
        print("\nВведений текст:")
        print(input_text)
        
        # Відсортовані слова
        sorted_words = sort_words(input_text)
        
        print("\nВідсортовані слова:")
        print(sorted_words)
        
        print("\nКількість слів:", len(sorted_words))

if __name__ == "__main__":
    main()