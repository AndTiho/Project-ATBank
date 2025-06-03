import pytest

# Для processing
@pytest.fixture
def empty_list():
    return [{}]


@pytest.fixture
def my_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def same_date_list():
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def no_state_in_list():
    return [
        {"id": 41428829, "date": "2018-06-30T02:08:58.425572"},
        {"id": 939719570, "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-06-30T02:08:58.425572"},
        {"id": 615064591, "date": "2018-06-30T02:08:58.425572"},
    ]


@pytest.fixture
def no_data_list():
    return [
        {"id": 41428829, "state": "EXECUTED"},
        {"id": 939719570, "state": "EXECUTED"},
        {"id": 594226727, "state": "CANCELED"},
        {"id": 615064591, "state": "CANCELED"},
    ]


@pytest.fixture
def not_list():
    return 0

#Для widget

@pytest.fixture
def empty_data():
    return " "


@pytest.fixture
def letters_string():
    return "Был бы я программист, но"
