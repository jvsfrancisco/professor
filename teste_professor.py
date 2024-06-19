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
        resultado, professor = add_professor("João", 
["Centro", "Tijuca"], [8,12], 
['matematica', 'fisica'])
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertIsInstance(professor['id'], int)

    def test_get_professor(self):
        resultado, professor = get_professor(1)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertEqual(professor['nome'], 'João')
        self.assertEqual(professor['filiais'], ["Centro", "Tijuca"])
        self.assertEqual(professor['horario'], [8, 12])
        self.assertEqual(professor['cursos'], ['matematica', 'fisica'])

    def test_add_filial(self):
        resultado, professor = add_filial(1, 'Barra')
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertIn('Barra', professor['filiais'])

    def test_del_filial(self):
        resultado, professor = del_filial(1, 'Tijuca')
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertNotIn('Tijuca', professor['filiais'])
    
    def test_add_curso(self):
        resultado, professor = add_curso(1, 'quimica')
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertIn('quimica', professor['cursos'])
    
    def test_del_curso(self):
        resultado, professor = del_curso(1, 'fisica')
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertNotIn('fisica', professor['cursos'])
    
    def test_set_horario(self):
        resultado, professor = set_horario(1, 10, 14)
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertEqual(professor['horario'], (10, 14))
    
    def test_get_professores(self):
        resultado, professores = get_professores()
        self.assertEqual(resultado, OPERACAO_REALIZADA_COM_SUCESSO)
        self.assertIsInstance(professores, list)
        self.assertIsInstance(professores[0], dict)
        self.assertIn('João', [professor['nome'] for professor in professores])

if __name__ == '__main__':
    unittest.main()

