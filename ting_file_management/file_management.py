import sys


def txt_importer(path_file):

    if not path_file.endswith('.txt'):
        sys.stderr.write("Formato inválido")
        return []
    try:
        with open(path_file, 'r') as file:
            news = [linha.strip() for linha in file.readlines()]
            return news
    except FileNotFoundError:
        sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
        return []
