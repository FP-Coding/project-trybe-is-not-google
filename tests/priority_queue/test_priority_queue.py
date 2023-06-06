import pytest
from ting_file_management.priority_queue import PriorityQueue


@pytest.fixture
def files():
    return [
        {
            "nome_do_arquivo": "arquivo5.txt",
            "qtd_linhas": 7,
            "linhas_do_arquivo": [
                "Esta é a linha 1",
                "Esta é a linha 2",
                "Esta é a linha 3",
                "Esta é a linha 4",
                "Esta é a linha 5",
                "Esta é a linha 6",
                "Esta é a linha 7",
            ],
        },
        {
            "nome_do_arquivo": "arquivo1.txt",
            "qtd_linhas": 3,
            "linhas_do_arquivo": [
                "primeira linha",
                "segunda linha",
                "terceira linha",
            ],
        },
        {
            "nome_do_arquivo": "arquivo2.txt",
            "qtd_linhas": 5,
            "linhas_do_arquivo": [
                "linha 1",
                "linha 2",
                "linha 3",
                "linha 4",
                "linha 5",
            ],
        },
        {
            "nome_do_arquivo": "arquivo3.txt",
            "qtd_linhas": 2,
            "linhas_do_arquivo": ["linha A", "linha B"],
        },
        {
            "nome_do_arquivo": "arquivo6.txt",
            "qtd_linhas": 6,
            "linhas_do_arquivo": [
                "Linha 1",
                "Linha 2",
                "Linha 3",
                "Linha 4",
                "Linha 5",
                "Linha 6",
            ],
        },
        {
            "nome_do_arquivo": "arquivo4.txt",
            "qtd_linhas": 1,
            "linhas_do_arquivo": ["linha única"],
        },
    ]


def test_basic_priority_queueing(files):
    queueOne = PriorityQueue()
    for file in files:
        queueOne.enqueue(file)
    assert len(queueOne) == 6
    result_first_file = queueOne.search(0)
    result_last_file = queueOne.search(5)
    assert result_last_file == files[4]
    assert result_first_file == files[1]
    queueOne.dequeue()
    assert len(queueOne) == 5
    result_first_file_post_dequeue = queueOne.search(0)
    assert result_first_file_post_dequeue == files[3]
    with pytest.raises(IndexError):
        queueOne.search(-100)
