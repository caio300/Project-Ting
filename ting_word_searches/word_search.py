def exists_word(word, instance):
    output = []

    current_position = instance.search(0)

    for index, line in enumerate(current_position["linhas_do_arquivo"]):
        if word in line:
            output.append({
                "palavra": word,
                "arquivo": current_position["nome_do_arquivo"],
                "ocorrencias": [{"linha": index + 1}],
            })

    instance.dequeue()
    return output


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
