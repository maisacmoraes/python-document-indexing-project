import re


def exists_word(word, instance):
    search_results = []

    for file in instance._data:
        file_occurrences = [
            {"linha": line_number}
            for line_number, line in enumerate(
                file["linhas_do_arquivo"], start=1
            )
            if re.search(re.escape(word), line, re.I)
        ]

        if file_occurrences:
            file_info = {
                "palavra": word,
                "arquivo": file["nome_do_arquivo"],
                "ocorrencias": file_occurrences,
            }
            search_results.append(file_info)

    return search_results


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
