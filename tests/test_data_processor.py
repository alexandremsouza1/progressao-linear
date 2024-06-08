import unittest
import json
from src.data_processor import process_data
import pandas as pd
import numpy as np
import os

class TestProcessData(unittest.TestCase):

    def test_process_data(self):
      # Obtenha o caminho do diretório do arquivo de teste
      test_dir = os.path.dirname(os.path.abspath(__file__))
      # Construa o caminho para mock.json
      mock_json_path = os.path.join(test_dir, 'mock.json')
        # Carregar os dados do mock.json
      with open(mock_json_path, 'r') as f:
        mock_data = json.load(f)

        # Criar DataFrame a partir dos dados do mock
        df = pd.DataFrame(mock_data['Data'])

        # Chamar a função process_data
        X, y = process_data(df)

        # Verificar se os conjuntos de características (X) e alvos (y) estão corretos
        expected_X = df[['ChangeDay', 'Change3M', 'Volume']]
        expected_y = np.array([0, 0, 1])  # Valores esperados para o alvo (Up)
        pd.testing.assert_frame_equal(X, expected_X)
        np.testing.assert_array_equal(y, expected_y)

if __name__ == '__main__':
    unittest.main()