import sys
from ting_file_management.file_management import txt_importer


def is_alredy_in_process(path_file, instance):
    files = [
        instance.search(index)["nome_do_arquivo"]
        for index in range(len(instance))
    ]
    return path_file in files


def process(path_file, instance):
    if is_alredy_in_process(path_file, instance):
        return
    else:
        lines = txt_importer(path_file)
        info_file = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(lines),
            "linhas_do_arquivo": lines,
        }
        instance.enqueue(info_file)
        print(info_file, file=sys.stdout)


def remove(instance):
    if len(instance) == 0:
        print("Não há elementos", file=sys.stdout)
    else:
        path_file = instance.dequeue()["nome_do_arquivo"]
        print(f"Arquivo {path_file} removido com sucesso")


def file_metadata(instance, position):
    try:
        content = instance.search(position)
    except IndexError:
        print("Posição inválida", file=sys.stderr)
    else:
        print(content, file=sys.stdout)
