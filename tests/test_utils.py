from unittest import mock
from src.utils import json_to_python_data
import pytest
from unittest.mock import patch, mock_open
import json


@pytest.mark.parametrize(
    "path, expected_result", [(0, []), ("", []), (1.5, []), ("not_a path", []), (None, []), ([], [])]
)
def test_all_errors(path, expected_result):
    assert json_to_python_data(path) == expected_result

# transactions_data взята из conftest.py
def test_correct_work(transactions_data):
  with patch('builtins.open', mock_open(read_data=json.dumps(transactions_data))):
    result = json_to_python_data('any_path')
    assert result == transactions_data
