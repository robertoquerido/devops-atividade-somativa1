import unittest

from saudacao import criar_saudacao


class TestSaudacao(unittest.TestCase):
    def test_nome_informado(self):
        self.assertEqual(
            criar_saudacao("Roberto"),
            "Olá, Roberto! Bem-vindo ao DevOps."
        )

    def test_nome_vazio(self):
        self.assertEqual(
            criar_saudacao(""),
            "Olá, Visitante! Bem-vindo ao DevOps."
        )

    def test_remove_espacos(self):
        self.assertEqual(
            criar_saudacao("  Roberto  "),
            "Olá, Roberto! Bem-vindo ao DevOps."
        )

    def test_apenas_espacos(self):
        self.assertEqual(
            criar_saudacao("   "),
            "Olá, Visitante! Bem-vindo ao DevOps."
        )


if __name__ == "__main__":
    unittest.main()