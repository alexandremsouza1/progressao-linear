import unittest
from unittest.mock import patch
from src.data_fetcher import fetch_data
import pandas as pd

class TestDataFetcher(unittest.TestCase):

    @patch('src.data_fetcher.requests.get')
    def test_fetch_data(self, mock_get):
        # Mock da resposta da solicitação
        mock_response = {
            "Data": [
                {"id": 1, "name": "Item 1"},
                {"id": 2, "name": "Item 2"}
            ]
        }
        
        # Configurando o retorno do mock da solicitação
        mock_get.return_value.json.return_value = mock_response

        # Chamando a função fetch_data
        df = fetch_data()

        # Verificando se o DataFrame retornado está correto
        expected_df = pd.DataFrame(mock_response['Data'])
        pd.testing.assert_frame_equal(df, expected_df)

if __name__ == '__main__':
    unittest.main()
