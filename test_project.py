from project import connection
from project import input_parser
from project import filter_by_city
from project import filter_by_pollutant
import pytest




def test_connection():
    with pytest.raises(SystemExit):
        assert connection(0)
        assert connection(-1)


def test_input_parser():
    with pytest.raises(SystemExit):
        assert input_parser(["xxxxx.py"])
        assert input_parser(["xxxxx.py" ,"-l"])


def test_filter_by_city():
        obj = connection(10000)
        assert filter_by_city(connection(10000),[["xxxxxx"]]) == 0
        assert filter_by_city(obj,[["raipur"]]) == 27
        assert filter_by_city(obj,[["chennai"]]) == 45
        assert filter_by_city(obj,[["chennai" ,"raipur"]]) == 72



def test_filter_by_pollutant():
        obj = connection(10000)
        assert filter_by_pollutant(connection(10000),[["xxxxxx"]]) == 0
        assert filter_by_pollutant(obj,[["nh3"]]) == 430
        assert filter_by_pollutant(obj,[["ozone"]]) == 464
        assert filter_by_pollutant(obj,[["ozone" , "nh3"]]) == 894



def filter_by_city_and_pollutant():
        obj = connection(10000)
        assert filter_by_pollutant(connection(10000),[["xxxxxx"]],[["yyyy"]]) == 0
        assert filter_by_pollutant(obj,[["chennai" ,"raipur"]],[["ozone" , "nh3"]]) == 22

