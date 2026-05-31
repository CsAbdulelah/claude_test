"""
CLI entry point: python -m portfolio.tracker

Run with current prices to see live P&L vs S&P 500.
Pass prices as  TICKER=PRICE  args, e.g.:
  python -m portfolio.tracker NVDA=140 AVGO=255 META=660 LLY=780 LMT=490 PLTR=130 SPY=598
"""

import sys
from datetime import date
from portfolio.initial_allocation import build_initial_portfolio, START_DATE
from portfolio.benchmark import Benchmark


def parse_prices(args: list[str]) -> dict[str, float]:
    prices = {}
    for arg in args:
        if "=" in arg:
            ticker, price = arg.split("=", 1)
            prices[ticker.upper()] = float(price)
    return prices


def main():
    prices = parse_prices(sys.argv[1:])

    portfolio = build_initial_portfolio()
    benchmark = Benchmark(start_date=START_DATE)

    for ticker, price in prices.items():
        if ticker == "SPY":
            benchmark.update_price(price)
        else:
            portfolio.update_price(ticker, price)

    stops = portfolio.check_stop_losses()

    print("=" * 80)
    print(f"  PORTFOLIO TRACKER  |  As of {date.today()}")
    print("=" * 80)
    print(portfolio.summary())
    print()
    print(benchmark.summary(portfolio.total_return_pct))

    if stops:
        print(f"\n*** STOP-LOSS ALERT: {', '.join(stops)} breached -15% — review immediately ***")


if __name__ == "__main__":
    main()
