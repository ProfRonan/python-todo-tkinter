"""Esse arquivo testa o arquivo gerenciador_tarefas.py"""

import unittest  # para criar o caso de teste

import gerenciador_tarefas as gt


class TestGerenciador(unittest.TestCase):
    """Classe para testar o módulo gerenciador_tarefas.py"""

    def setUp(self):
        """Inicializa os casos de teste"""
        gt.lista_de_tarefas = []

    def test_adiciona_tarefas_lista_vazia(self):
        """Testa se é possível adicionar uma tarefa à lista vazia"""
        tarefa = {"prioridade": True, "texto": "Tarefa 1"}
        gt.adicionar_tarefa(tarefa["prioridade"], tarefa["texto"])
        self.assertEqual(gt.lista_de_tarefas, [tarefa])

    def test_adiciona_tarefas_lista_elementos(self):
        """Testa se é possível adicionar uma tarefa à lista com alguns elementos"""
        tarefas = [
            {"prioridade": True, "texto": "Tarefa 1"},
            {"prioridade": False, "texto": "Tarefa 2"},
            {"prioridade": True, "texto": "Tarefa 3"},
        ]
        for tarefa in tarefas:
            gt.adicionar_tarefa(tarefa["prioridade"], tarefa["texto"])
        self.assertEqual(gt.lista_de_tarefas, tarefas)

    def test_adiciona_tarefa_prioridade_invalida(self):
        """Testa se é possível adicionar uma tarefa à com prioridade inválida"""
        tarefa = {"prioridade": "prioridade inválida", "texto": "Tarefa 1"}
        self.assertRaises(
            ValueError, gt.adicionar_tarefa, tarefa["prioridade"], tarefa["texto"]
        )

    def test_adiciona_tarefa_ja_existente(self):
        """Testa se é possível adicionar uma tarefa com mesmo nome de outra"""
        tarefa = {"prioridade": True, "texto": "Tarefa 1"}
        gt.adicionar_tarefa(tarefa["prioridade"], tarefa["texto"])
        self.assertRaises(
            ValueError, gt.adicionar_tarefa, tarefa["prioridade"], tarefa["texto"]
        )

    def test_remove_tarefa_lista_vazia(self):
        """Testa se é possível remover uma tarefa da lista vazia"""
        self.assertRaises(ValueError, gt.remove_tarefas, (0,))

    def test_remove_tarefa_lista_com_elementos(self):
        """Testa se é possível remover uma tarefa da lista sem ter o elemento nela"""
        tarefa = {"prioridade": True, "texto": "Tarefa 1"}
        gt.adicionar_tarefa(tarefa["prioridade"], tarefa["texto"])
        self.assertRaises(ValueError, gt.remove_tarefas, (1,))

    def test_remove_tarefa_lista_varias(self):
        """Testa se é possível remover várias tarefas da lista"""
        tarefas = [
            {"prioridade": True, "texto": "Tarefa 1"},
            {"prioridade": False, "texto": "Tarefa 2"},
            {"prioridade": True, "texto": "Tarefa 3"},
            {"prioridade": False, "texto": "Tarefa 4"},
        ]
        for tarefa in tarefas:
            gt.adicionar_tarefa(tarefa["prioridade"], tarefa["texto"])
        gt.remove_tarefas((1, 3))
        self.assertEqual(gt.lista_de_tarefas, [tarefas[0], tarefas[2]])

    def test_ordena_prioridade(self):
        """
        Testa se é possível ordenar as tarefas por prioridade
        """
        tarefas = [
            {"prioridade": True, "texto": "C"},
            {"prioridade": False, "texto": "B"},
            {"prioridade": True, "texto": "A"},
            {"prioridade": False, "texto": "D"},
        ]
        for tarefa in tarefas:
            gt.adicionar_tarefa(tarefa["prioridade"], tarefa["texto"])
        gt.ordena_por_prioridade()
        self.assertEqual(
            gt.lista_de_tarefas, [tarefas[2], tarefas[0], tarefas[1], tarefas[3]]
        )
