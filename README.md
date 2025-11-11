# Stock Viewer

A simple command-line tool for quickly checking real-time stock data using Python.

## Overview
Stock Viewer retrieves live market information for one or more stock tickers and displays selected metrics in a clean, readable table. You can run it by passing tickers directly from the command line, or enter them interactively. An optional --metrics flag allows customizing which metrics to display, and results can be saved to a CSV file.

## Features

Real-time financial data via yfinance

Supports multiple tickers

Optional -m / --metrics flag to choose which fields to display

Clean table formatting using tabulate

Market capitalization abbreviated with millify

Optional CSV export

## Installation
Install dependencies using requirements.txt:
pip install -r requirements.txt

## Usage

### Default Metrics
python project.py AAPL MSFT TSLA

### Select Specific Metrics
python project.py AAPL MSFT -m open dayHigh marketCap

### Interactive Mode
python project.py
Which stock ticker would you like to check? (-n to proceed)

## Example Output

AAPL

| Metric        | Value  |
|---------------|--------|
| lastPrice     | 189.41 |
| previousClose | 188.93 |
| open          | 189.75 |
| dayHigh       | 191.11 |
| dayLow        | 188.35 |
| marketCap     | 2.9T   |

(Values vary depending on market data.)

## CSV Export
Would you like to save this to a CSV? (Y/N)
What .csv do you want to save to? mydata.csv

## File Structure
project.py
README.md
requirements.txt

## Technologies Used

Python

yfinance

argparse

tabulate

millify

Built as final project for Harvard CS50P: Introduction to Programming with Python.
