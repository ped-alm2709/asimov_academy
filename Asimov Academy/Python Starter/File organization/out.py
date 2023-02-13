import os


cwd = os.getcwd()

# lista de diretórios criados com o in.py
folder_list = [i for i in os.listdir(cwd) if os.path.isdir(i)]

for folder in folder_list:
    # caminho até as pastas
    path = os.path.join(cwd, folder)

    # caminho até os arquivos dentro das pastas
    files = os.listdir(path)

    for item in files:
        from_path = os.path.join(path, item)
        to_path = os.path.join(cwd, item)
        os.replace(from_path, to_path)

    os.rmdir(path)
