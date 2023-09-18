import os
import shutil


def delete_mm_folders(folder_path):
    a = 0
    b = 0
    for root, dirs, files in os.walk(folder_path, topdown=False):
        for directory in dirs:
            if directory == 'mm':
                folder_to_delete = os.path.join(root, directory)
                try:
                    shutil.rmtree(folder_to_delete)  
                    a += 1
                except OSError as e:
                    b += 1
    return f"DEl: {a} , NOT DEL {b}"

wwwf = '../www'

cvb = delete_mm_folders(wwwf)
print(cvb)
