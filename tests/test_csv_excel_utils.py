from src.csv_excel_utils import csv_to_python_data, excel_to_python_data
from unittest.mock import patch, mock_open
import pytest
import pandas as pd


@pytest.mark.parametrize(
    "path, expected_result", [(0, []), ("", []), (1.5, []), ("not_a path", []), (None, []), ([], [])]
)
def test_all_errors_csv(path, expected_result):
    assert csv_to_python_data(path) == expected_result


# csv_data взята из conftest.py
def test_correct_work(csv_data):
    with patch("builtins.open", mock_open(read_data=csv_data)):
        result = csv_to_python_data("any_path")
        assert result == [
            {
                "id": "650703",
                "state": "EXECUTED",
                "date": "2023-09-05T11:30:32Z",
                "amount": "16210",
                "currency_name": "Sol",
                "currency_code": "PEN",
                "from": "Счет 58803664561298323391",
                "to": "Счет 39745660563456619397",
                "description": "Перевод организации",
            }
        ]


@pytest.mark.parametrize(
    "path, expected_result", [(0, []), ("", []), (1.5, []), ("not_a path", []), (None, []), ([], [])]
)
def test_all_errors_excel(path, expected_result):
    assert excel_to_python_data(path) == expected_result


# my_list взят из conftest.py
def test_excel_to_python_data(my_list):
    mock_df = pd.DataFrame(my_list)
    with patch("pandas.read_excel", return_value=mock_df):
        result = excel_to_python_data("any_path")
        assert result == my_list
