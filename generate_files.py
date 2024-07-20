import os
import random
import string

# Папка для зберігання тестових файлів
os.makedirs('test_files', exist_ok=True)

# Кількість файлів та ключових слів
num_files = 10
keywords = ["example", "test", "search", "keyword", "file"]
max_keywords_per_file = 100


def generate_random_text(length=1000):
    """Генерує випадковий текст заданої довжини."""
    letters = string.ascii_lowercase + ' '
    return ''.join(random.choice(letters) for i in range(length))


def generate_test_files(num_files, keywords, max_keywords_per_file):
    for i in range(num_files):
        filename = os.path.join('test_files', f'file{i + 1}.txt')
        text = generate_random_text()

        # Додаємо випадкові ключові слова
        for _ in range(random.randint(1, max_keywords_per_file)):
            keyword = random.choice(keywords)
            position = random.randint(0, len(text) - 1)
            text = text[:position] + keyword + text[position + len(keyword):]

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(text)


generate_test_files(num_files, keywords, max_keywords_per_file)
print(f"Generated {num_files} test files with random text and keywords in 'test_files' directory.")
