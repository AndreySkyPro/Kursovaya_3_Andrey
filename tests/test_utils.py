import pytest

from testing_data import right_data
from utils import get_data, get_filtred_data, get_last_values, get_formated_data


def test_get_data():
    data = get_data()
    assert isinstance(data, list)

def test_get_filtred_data():
    data = right_data()
    assert len(get_filtred_data(data)) == 76

def test_get_last_values():
    data = get_last_values(right_data(), 2)
    assert [x['date'] for x in data] == ['2019-12-07T06:17:14.634890', '2019-11-19T09:22:25.899614']

def test_get_formated_data():
    data = get_formated_data(right_data()[:3])
    assert data[0] == "\n26.08.2019 Перевод организации\nMaestro 1596 83** **** 5199 -> Счет **9589\n31957.58 руб."
    assert data[1] == "\n03.07.2019 Перевод организации\nMasterCard 7158 30** **** 6758 -> Счет **5560\n8221.37 USD"