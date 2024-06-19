# teste_professor.py
import unittest
from professor import *

OPERACAO_REALIZADA_COM_SUCESSO = 0
ARQUIVO_NAO_ENCONTRADO = 30
ARQUIVO_EM_FORMATO_INVALIDO = 31
ERRO_NA_ESCRITA_DO_ARQUIVO = 32
PROFESSOR_NAO_ENCONTRADO = 17
FILIAL_JA_ADICIONADA = 18
FILIAL_NAO_EXISTENTE = 19
CURSO_JA_ADICIONADO = 20
CURSO_NAO_EXISTENTE = 21
HORARIO_INVALIDO = 22

class TestProfessor(unittest.TestCase):
    
    def setUp(self):
        inicializar()
    
    def tearDown(self):
        finalizar()

    def test_inicializar(self):
        resultado = inicializar()
        self.assertIn(resultado, [OPERACAO_REALIZADA_COM_SUCESSO, ARQUIVO_NAO_ENCONTRADO])

    def test_finalizar(self):
        resultado = finalizar()
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)

    def test_add_professor(self):
        resultado, id_professor = add_professor("Dr. Smith")
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertIsInstance(id_professor, int)

    def test_get_professor(self):
        _, id_professor = add_professor("Dr. Smith")
        resultado, professor = get_professor(id_professor)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertEqual(professor['nome'], "Dr. Smith")

    def test_add_curso(self):
        _, id_professor = add_professor("Dr. Smith")
        resultado = add_curso(id_professor, "Matemática")
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)

    def test_del_curso(self):
        _, id_professor = add_professor("Dr. Smith")
        add_curso(id_professor, "Matemática")
        resultado = del_curso(id_professor, "Matemática")
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)

    def test_set_horario(self):
        _, id_professor = add_professor("Dr. Smith")
        resultado = set_horario(id_professor, 9, 17)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)

    def test_add_filial(self):
        _, id_professor = add_professor("Dr. Smith")
        resultado = add_filial(id_professor, 1)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)

    def test_del_filial(self):
        _, id_professor = add_professor("Dr. Smith")
        add_filial(id_professor, 1)
        resultado = del_filial(id_professor, 1)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)

    def test_get_professores(self):
        add_professor("Dr. Smith")
        resultado, professores = get_professores()
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertIsInstance(professores, list)
        self.assertGreaterEqual(len(professores), 1)

if __name__ == '__main__':
    unittest.main()
