import pytest
from project import parse_args
from project import verify_input
from project import display_data

def test_parse_args():
    args = parse_args(["AAPL", "MSFT"])
    assert args.tickers == ["AAPL", "MSFT"]
    assert args.metrics == None
    args = parse_args(["A", "B", "C", "-m", "aaa", "abc"])
    assert args.tickers == ["A", "B", "C"]
    assert args.metrics == ["aaa", "abc"]


def test_verify_input():
    test = verify_input("AAPL", "FAKETICKER123")
    assert len(test) == 1
    assert test[0]["Ticker"] == "AAPL"


def test_display_data(capsys):
    data = {"Ticker": "AAPL", "Info": {"dayLow": 100, "dayHigh": 110}}
    display_data(data)
    out, err = capsys.readouterr()
    assert "AAPL" in out
    assert "100" in out
    assert "110" in out

