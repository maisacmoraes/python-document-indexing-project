from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()
    data = {"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 3}
    priority_queue.enqueue(data)
    assert len(priority_queue) == 1
    assert priority_queue.dequeue() == data
    assert len(priority_queue) == 0

    data1 = {"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 9}
    data2 = {"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 4}
    data3 = {"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 2}
    data4 = {"nome_do_arquivo": "arquivo_teste.txt", "qtd_linhas": 5}

    priority_queue.enqueue(data1)
    priority_queue.enqueue(data2)
    priority_queue.enqueue(data3)
    priority_queue.enqueue(data4)

    assert priority_queue.search(0) == data2
    assert priority_queue.search(1) == data3
    assert priority_queue.search(2) == data1

    with pytest.raises(IndexError):
        priority_queue.search(5)
