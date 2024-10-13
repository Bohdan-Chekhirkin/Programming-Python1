# utils.py

def is_even_or_ends_with_7(num):
    """Перевіряє, чи є число парним або закінчується на 7."""
    return num % 2 == 0 or str(num).endswith('7')

def translate(text, lang):
    """Переклад тексту на вказану мову (для демонстрації)."""
    translations = {
        'en': {
            'result': 'The result is: ',
            'enter_numbers': 'Please enter two integers (a and b): ',
            'invalid_language': 'Invalid language selected, defaulting to Ukrainian.',
        },
        'uk': {
            'result': 'Результат: ',
            'enter_numbers': 'Будь ласка, введіть два цілих числа (a та b): ',
            'invalid_language': 'Некоректна мова, за замовчуванням використовується українська.',
        }
    }
    return translations.get(lang, translations['uk']).get(text, text)