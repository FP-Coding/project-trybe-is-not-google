def search_word(lines, word, type):
    result_list = {"complete": list(), "simples": list()}

    for line in lines:
        if word.lower() in line.lower():
            if type == "complete":
                result_list["complete"].append(
                    {"linha": lines.index(line) + 1, "conteudo": line}
                )
            else:
                result_list["simples"].append({"linha": lines.index(line) + 1})
    return result_list[type]


def exists_word(word, instance):
    search_result = list()
    for index in range(len(instance)):
        file = instance.search(index)
        occurrences = search_word(
            file["linhas_do_arquivo"], word, type="simples"
        )
        if len(occurrences) > 0:
            search_result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return search_result


def search_by_word(word, instance):
    search_result = list()
    for index in range(len(instance)):
        file = instance.search(index)
        occurrences = search_word(
            file["linhas_do_arquivo"], word, type="complete"
        )
        if len(occurrences) > 0:
            search_result.append(
                {
                    "palavra": word,
                    "arquivo": file["nome_do_arquivo"],
                    "ocorrencias": occurrences,
                }
            )
    return search_result
