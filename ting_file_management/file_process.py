import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    for i in range(len(instance)):
        if instance.search(i)['nome_do_arquivo'] == path_file:
            return

    data = txt_importer(path_file)
    resp_obj = ({
        'nome_do_arquivo': path_file,
        'qtd_linhas': len(data),
        'linhas_do_arquivo': data,
    })

    instance.enqueue(resp_obj)
    sys.stdout.write(str(resp_obj))


def remove(instance):
    pass


def file_metadata(instance, position):
    try:
        data = str(instance.search(position))
        return sys.stdout.write(data)
    except IndexError:
        return sys.stderr.write("Posição inválida")
