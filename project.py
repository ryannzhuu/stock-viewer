import yfinance as yf
from typing import List, Dict
import argparse
from tabulate import tabulate
import csv
from millify import millify


metrics_to_show = ["lastPrice", "previousClose", "open", "dayHigh", "dayLow", "marketCap"]


def main():
    args = parse_args()
    global metrics_to_show
    if args.metrics:
        metrics_to_show = args.metrics
    tickers = []
    if not args.tickers:
        while True:
            x = input("Which stock ticker would you like to check? (-n to proceed) " )
            if x != "-n":
                tickers.append(x)
            else:
                break
    else:
        tickers = args.tickers
    tickers = verify_input(*tickers)
    for ticker in tickers:
        display_data(ticker)
    if tickers:
        savecsv = input("Would you like to save this to a CSV? (Y/N) ")
        if savecsv.strip().lower() in ("yes", "y", "ye"):
            save(tickers)


def parse_args(arg_list=None):
    """Parse command line arguments and return a Namespace object."""
    parser = argparse.ArgumentParser(description="Obtain data on stocks")
    parser.add_argument("tickers", nargs="*", help="tickers of the stocks you want to check")
    parser.add_argument("-m", "--metrics", nargs="+", help="stock metrics you would like to check")
    return parser.parse_args(arg_list)


def verify_input(*args) -> List[Dict[str, dict]]:
    """Return a list of valid ticker dictionaries from arguments provided
    Invalid tickers are skipped and a warning is printed.
    """
    ticker_list = []
    for arg in args:
        try:
            ticker = yf.Ticker(arg.strip().upper())
            info = dict(ticker.fast_info)
            ticker_list.append({"Ticker": arg.strip().upper(), "Info": info})
        except:
            print(f"Error with {arg}... Skipping. ")
    return ticker_list


def display_data(ticker_dict: Dict[str, dict]):
    """Print a formatted table of selected metrics for specific tickers.
    """
    global metrics_to_show
    print_dict = {}
    print(f"\n{ticker_dict['Ticker']}")
    for metric in metrics_to_show:
        if metric in ticker_dict["Info"]:
                if metric == "marketCap":
                    try:
                        print_dict[metric] = millify(ticker_dict["Info"][metric], precision=2, drop_nulls=False)
                    except:
                        print_dict[metric] = "N/A"
                else:
                    try:
                        print_dict[metric] = round(float(ticker_dict["Info"][metric]), 2)
                    except:
                        print_dict[metric] = "N/A"
        else:
            print_dict[metric] = "N/A"
    rows = print_dict.items()
    print(tabulate(rows, headers=["Metric", "Value"], tablefmt="github"))


def save(tickers):
    """Prompts the user for a CSV filename
    Saves ticker data to the given file.
    """
    while True:
        try:
            filename = input("What .csv do you want to save to? ")
            if not filename.strip().endswith(".csv"):
                raise ValueError
            break
        except ValueError:
            print("Invalid file name. ")

    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Ticker"] + metrics_to_show)
        for ticker in tickers:
            writer.writerow([ticker["Ticker"]] + [ticker["Info"].get(m, "N/A") for m in metrics_to_show])


if __name__ == "__main__":
    main()
