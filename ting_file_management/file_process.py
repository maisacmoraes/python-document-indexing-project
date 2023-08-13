from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    name_file = txt_importer(path_file)
    index = 0

    while index < len(instance):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return
        index += 1

    dicionario = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(name_file),
        "linhas_do_arquivo": name_file,
    }

    instance.enqueue(dicionario)
    sys.stdout.write(str(dicionario))


def remove(instance):
    if not instance:
        return sys.stdout.write("Não há elementos\n")

    path_file = instance.dequeue()["nome_do_arquivo"]
    sys.stdout.write(f"Arquivo {path_file} removido com sucesso\n")


def file_metadata(instance, position):
    try:
        value_to_be_returned = instance.search(position)
        return sys.stdout.write(str(value_to_be_returned))
    except IndexError:
        return sys.stderr.write("Posição inválida\n")
