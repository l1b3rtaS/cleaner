import os
import shutil

# Функция для удаления папок с именем 'mm'
def delete_mm_folders(folder_path):
    a = 0
    b = 0
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for directory in dirs:
            if directory == 'mm':
                folder_to_delete = os.path.join(root, directory)
                try:
                    shutil.rmtree(folder_to_delete)  # Удаление пустой папки
                    a += 1
                except OSError as e:
                    b += 1
    return f"DEl: {a} , NOT DEL {b}"
# Замените 'путь_к_папке_www' на фактический путь к вашей папке 'www'
wwwf = '../www'

delete_mm_folders(wwwf)