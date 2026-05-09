import os
import shutil
import time


PATH_TO_WATCH = os.path.join(os.path.expanduser('~'), 'Downloads')
CATEGORIES = {
    'Images': ['.jpg', '.png', '.gif'],
    'Docs': ['.pdf', '.docx', '.txt', ''],
    'Music': ['.mp3', '.wav']
}

def sort_files():
    for file in os.listdir(PATH_TO_WATCH):
        full_path = os.path.join(PATH_TO_WATCH, file)
        if os.path.isfile(full_path):
            ext = os.path.splitext(file)[1].lower()
            for cat, extensions in CATEGORIES.items():
                if ext in extensions:
                    dest_dir = os.path.join(PATH_TO_WATCH, cat)
                    os.makedirs(dest_dir, exist_ok=True)
                    shutil.move(full_path, os.path.join(dest_dir, file))
                    print(f"Сортировка: {file} -> {cat}")


def main():
    print(f"Слежу за папкой: {PATH_TO_WATCH}...")
    while True:
        try:
            sort_files()
        except Exception as e:
            print(f"Ошибка: {e}")
        
        time.sleep(30)

if __name__ == "__main__":
    main()