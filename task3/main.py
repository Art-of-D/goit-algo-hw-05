import timeit
import chardet
from pathlib import Path
from algorithm.bm import boyer_moore_search
from algorithm.kmp import kmp_search
from algorithm.rk import rabin_karp_search

def detect_encoding(file_path):
    """Визначає кодування файлу"""
    with open(file_path, 'rb') as file:
        raw_data = file.read(10000)
    result = chardet.detect(raw_data)
    return result['encoding'] if result['encoding'] else 'utf-8'

def read_file(file_path):
    file_path = file_path.resolve()
    if not file_path.exists():
        print(f"Помилка: Файл '{file_path}' не знайдено.")
        return None
    if not file_path.is_file():
        print(f"Помилка: '{file_path}' не є файлом.")
        return None
    
    encoding = detect_encoding(file_path)

    try:
        with open(file_path, 'r', encoding=encoding) as file:
            return file.read()
    except IOError as e:
        print(f"Помилка доступу до файлу '{file_path}': {e}")
        return None

def analyze_text(text, pattern):
    
    if text is None:
        print("Неможливо проаналізувати: текст не було зчитано.")
        return
    
    bm_time = timeit.timeit(lambda: boyer_moore_search(text, pattern), number=10)
    kmp_time = timeit.timeit(lambda: kmp_search(text, pattern), number=10)
    rk_time = timeit.timeit(lambda: rabin_karp_search(text, pattern), number=10)
    print("-"*10)
    print(f"Алгоритм Боєра-Мура: {bm_time:.6f} сек")
    print(f"Алгоритм Кнута-Морріса-Пратта: {kmp_time:.6f} сек")
    print(f"Алгоритм Рабіна-Карпа: {rk_time:.6f} сек")
    
    bm_result = boyer_moore_search(text, pattern)
    kmp_result = kmp_search(text, pattern)
    rk_result = rabin_karp_search(text, pattern)

    print("\nЗнайдені збіги:")
    print(f"Боєра-Мура: {bm_result}")
    print(f"Кнута-Морріса-Пратта: {kmp_result}")
    print(f"Рабіна-Карпа: {rk_result}")
    print("-"*10)

def main():
    
    text1 = Path("./task3/data/1.txt")
    text2 = Path("./task3/data/2.txt")
    pattern = input("Введіть підрядок для пошуку: \n")

    while pattern not in ["exit", "quit", "0"]:
      for text in [text1, text2]:
        rd = read_file(text)
        analyze_text(rd, pattern)

      pattern = input("Введіть підрядок для пошуку: \n(якщо потрібно вийти, введіть 'exit', 'quit' або '0')\n")

if __name__ == "__main__":
    main()