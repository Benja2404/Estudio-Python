import unittest
import cambia_texto

class ProbarCambiaTexto(unittest.TestCase):
    def test_mayusculas(self):
        texto = 'hola'
        resultado = cambia_texto.todo_mayusculas(texto)
        self.assertEqual(resultado, 'hOla')



if __name__ == '__main__':
    unittest.main()