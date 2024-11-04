import sys

def compare_files(file1, file2):
    # Читаем содержимое обоих файлов и предварительно обрабатываем строки
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = set(line.strip().lower() for line in f1 if line.strip())  # Учитываем регистр и убираем пустые строки
        lines2 = set(line.strip().lower() for line in f2 if line.strip())  # Учитываем регистр и убираем пустые строки

    # Получаем строки, которые есть только в первом файле
    new_lines = lines1 - lines2
    new_lines2 = lines2 - lines1

    # Выводим строки только новых строк из первого файла (то что новое)
    for line in new_lines:
        print("+" ,line)
    
    # Выводим строки только новых строк из второго файла (то что новое)
    for line2 in new_lines2:
        print("-" ,line2)

# Пример использования
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python diffy.py file1 file2")
        sys.exit(1)

    compare_files(sys.argv[1], sys.argv[2])
