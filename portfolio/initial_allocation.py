"""
Initial $1000 allocation — executed 2026-05-31.
Shariah-compliant revision — executed 2026-05-31.

Strategy rationale:
  - 6 concentrated positions across 3 secular themes — ALL Shariah compliant
  - No broad index exposure (we're trying to BEAT the index, not match it)
  - 10% cash reserve for opportunistic adds or replacing stopped-out positions
  - Stop-loss at -15% per position; no target on upside (let winners run)

Compliance changes from original allocation:
  LMT  REMOVED — weapons manufacturer, primary business violation (clear haram)
  PLTR RESTORED — software/analytics company; does NOT manufacture weapons;
                  analogous to Microsoft serving government clients (compliant)
  MSFT ADDED   — replaces LMT slot; cloud/AI/productivity; passes AAOIFI screens

Themes:
  1. AI infrastructure (NVDA, AVGO — picks-and-shovels)
  2. AI monetisation & cloud (META, MSFT, PLTR)
  3. Healthcare innovation (LLY — GLP-1 demand still early innings)

Tickers and approximate prices as of 2026-05-31:
  NVDA  ~$135   AI infrastructure
  AVGO  ~$240   AI networking ASICs
  META  ~$640   AI-monetised advertising at scale
  LLY   ~$770   GLP-1 / obesity drug leader
  MSFT  ~$460   Cloud (Azure) + AI (Copilot); replaces LMT
  PLTR  ~$125   AI/data analytics platform; software = halal
  Cash  reserve  ~$74
"""

from datetime import date
from portfolio.strategy import Portfolio

START_DATE = date(2026, 5, 31)

# (ticker, shares, price, sector, one-line thesis)
INITIAL_TRADES = [
    ("NVDA", 1.300, 135.00, "AI Infrastructure",  "GPU monopoly for AI training & inference"),
    ("AVGO", 0.625, 240.00, "AI Infrastructure",  "Custom AI ASICs + networking; recurring FCF"),
    ("META", 0.235, 640.00, "AI Monetisation",    "Best ad-tech moat; Llama = AI optionality"),
    ("LLY",  0.195, 770.00, "Healthcare Innov.",  "GLP-1 demand far exceeds current supply"),
    ("MSFT", 0.326, 460.00, "Cloud / AI",         "Azure #2 cloud; Copilot AI monetisation"),
    ("PLTR", 1.200, 125.00, "AI / Data Analytics","AIP platform; fastest-growing commercial segment"),
]


def build_initial_portfolio() -> Portfolio:
    p = Portfolio(start_date=START_DATE, starting_cash=1000.0)
    for ticker, shares, price, sector, thesis in INITIAL_TRADES:
        p.buy(ticker, shares, price, sector, thesis)
    return p


if __name__ == "__main__":
    p = build_initial_portfolio()
    print("=" * 80)
    print("  $1000 PORTFOLIO — INITIAL ALLOCATION  |  vs S&P 500 challenge")
    print(f"  Start date: {START_DATE}")
    print("=" * 80)
    print(p.summary())
    print(f"\nCash remaining : ${p.cash:.2f}")
    print(f"Invested       : ${p.total_value - p.cash:.2f}")
    print(f"Total          : ${p.total_value:.2f}")
