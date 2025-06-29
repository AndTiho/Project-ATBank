import pytest
from src.decorators import log

# Тест успешного выполнения функции без файла лога
def test_function_no_file(capsys):
    @log(filename='')
    def func(x, y):
        return x + y

    func(1, 2)

    captured = capsys.readouterr()
    output = captured.out
    assert 'ok. Result = 3' in output
    assert 'Start at' in output
    assert 'Ended at' in output


# Тест обработки исключения без файла лога
def test_exception_no_file(capsys):
    @log(filename='')
    def func(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        func(1, 0)

    captured = capsys.readouterr()
    output = captured.out
    assert 'division by zero' in output
    assert 'Inputs: (1, 0)' in output
    assert 'Start at' in output
    assert 'Ended at' in output


# Тест успешного выполнения функции с записью в файл лога
def test_function_with_file(tmp_path):
    log_file = tmp_path / "test_log.txt"
    @log(filename=str(log_file))
    def func(x, y):
        return x + y

    func(1, 2)

    with open(log_file, 'r') as f:
        log_content = f.read()

        assert "Start at" in log_content
        assert "func ok" in log_content
        assert "Ended at" in log_content

# Тест обработки исключения с записью в файл лога
def test_exception_with_file(tmp_path):
    log_file = tmp_path / "test_log.txt"
    @log(filename=str(log_file))
    def func(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        func(1, 0)

    with open(log_file, 'r') as f:
        log_content = f.read()

    assert 'division by zero' in log_content
    assert 'Inputs: (1, 0)' in log_content
    assert 'Start at' in log_content
    assert 'Ended at' in log_content