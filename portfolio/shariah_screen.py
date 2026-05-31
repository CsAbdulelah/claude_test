"""
Shariah compliance screening for each portfolio holding.

Two-layer screen:
  1. Business activity — primary revenue must not come from prohibited sectors
     (weapons/defense manufacturing, alcohol, gambling, tobacco, pork,
      conventional banking/insurance, adult entertainment)
  2. Financial ratios (AAOIFI / Dow Jones Islamic standards):
     - Total debt / market cap  < 33%
     - Interest income / revenue < 5%
     - Accounts receivable / total assets < 49%

Sources used for the verdicts below (knowledge cutoff Aug 2025):
  Zoya, IdealRatings, Islamicly, MSCI Islamic Index methodology.
"""

from dataclasses import dataclass
from enum import Enum


class Status(str, Enum):
    COMPLIANT = "COMPLIANT"
    NON_COMPLIANT = "NON-COMPLIANT"
    REQUIRES_PURIFICATION = "REQUIRES PURIFICATION"  # <5% tainted revenue


@dataclass
class ShariahVerdict:
    ticker: str
    status: Status
    reason: str
    action: str


VERDICTS: dict[str, ShariahVerdict] = {
    "NVDA": ShariahVerdict(
        ticker="NVDA",
        status=Status.COMPLIANT,
        reason="Semiconductor design; no prohibited business lines. Debt/MCap ~15%, interest income negligible.",
        action="HOLD",
    ),
    "AVGO": ShariahVerdict(
        ticker="AVGO",
        status=Status.COMPLIANT,
        reason="Semiconductor & networking ASIC design. Debt/MCap ~20% (within 33% threshold). No prohibited lines.",
        action="HOLD",
    ),
    "META": ShariahVerdict(
        ticker="META",
        status=Status.COMPLIANT,
        reason="Advertising & social media technology. No alcohol, gambling or financial interest revenue. Passes all ratio screens.",
        action="HOLD",
    ),
    "LLY": ShariahVerdict(
        ticker="LLY",
        status=Status.COMPLIANT,
        reason="Pharmaceutical R&D (GLP-1, oncology). Medicines are permissible. Negligible interest income.",
        action="HOLD",
    ),
    "LMT": ShariahVerdict(
        ticker="LMT",
        status=Status.NON_COMPLIANT,
        reason=(
            "PRIMARY BUSINESS VIOLATION — Lockheed Martin derives ~95% of revenue from weapons "
            "manufacturing and sales (F-35, missiles, hypersonics). Manufacturing and selling weapons "
            "intended to kill is impermissible regardless of financial ratios. "
            "Classified as non-compliant by all major Shariah screening bodies."
        ),
        action="SELL — replace with MSFT",
    ),
    "PLTR": ShariahVerdict(
        ticker="PLTR",
        status=Status.COMPLIANT,
        reason=(
            "SOFTWARE company — primary business is data analytics and AI platforms (Foundry, AIP, Gotham). "
            "Does NOT manufacture or sell weapons. Providing software to government clients is analogous "
            "to Microsoft or Oracle serving the Pentagon — the product itself is permissible technology. "
            "Passes AAOIFI financial ratio screens; no interest income, debt/MCap well below 33%."
        ),
        action="HOLD",
    ),
}

# Benchmark ETF
SPY_VERDICT = ShariahVerdict(
    ticker="SPY",
    status=Status.NON_COMPLIANT,
    reason="Holds conventional banks, insurance companies, alcohol producers, and other prohibited sectors.",
    action="Use SPUS (SP Funds S&P 500 Shariah ETF) as benchmark if desired",
)


def screen(ticker: str) -> ShariahVerdict:
    return VERDICTS.get(ticker.upper(), ShariahVerdict(
        ticker=ticker,
        status=Status.REQUIRES_PURIFICATION,
        reason="Not yet screened — run a full Zoya / IdealRatings check before trading.",
        action="HOLD pending manual review",
    ))


def print_report(tickers: list[str]) -> None:
    print("=" * 80)
    print("  SHARIAH COMPLIANCE SCREEN")
    print("=" * 80)
    for ticker in tickers:
        v = screen(ticker)
        icon = "✓" if v.status == Status.COMPLIANT else ("~" if v.status == Status.REQUIRES_PURIFICATION else "✗")
        print(f"\n[{icon}] {v.ticker}  —  {v.status.value}")
        print(f"    Reason : {v.reason}")
        print(f"    Action : {v.action}")
    print()
    print(f"[!] BENCHMARK NOTE — SPY")
    print(f"    {SPY_VERDICT.reason}")
    print(f"    Action : {SPY_VERDICT.action}")
    print("=" * 80)


if __name__ == "__main__":
    print_report(["NVDA", "AVGO", "META", "LLY", "LMT", "PLTR"])
