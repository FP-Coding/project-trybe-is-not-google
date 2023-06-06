import sys


def txt_importer(path_file):
    try:
        if not path_file.endswith(".txt"):
            raise ValueError
        with open(path_file) as file:
            content = file.read()
        return content.split("\n")
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
    except ValueError:
        print("Formato inválido", file=sys.stderr)
