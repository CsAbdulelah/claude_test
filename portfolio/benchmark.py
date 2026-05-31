"""
S&P 500 benchmark tracker — compares portfolio performance against a
passive $1000 SPY investment starting on the same date.
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Benchmark:
    start_date: date
    starting_value: float = 1000.0
    # SPY price on 2026-05-31 (approximate); update via update_price() on each check-in
    _start_price: float = 595.00
    _current_price: float = 595.00

    @property
    def shares(self) -> float:
        return self.starting_value / self._start_price

    @property
    def current_value(self) -> float:
        return self.shares * self._current_price

    @property
    def return_pct(self) -> float:
        return (self.current_value - self.starting_value) / self.starting_value * 100

    def update_price(self, price: float) -> None:
        self._current_price = price

    def vs_portfolio(self, portfolio_return_pct: float) -> float:
        """Alpha: portfolio return minus benchmark return (percentage points)."""
        return portfolio_return_pct - self.return_pct

    def summary(self, portfolio_return_pct: float) -> str:
        alpha = self.vs_portfolio(portfolio_return_pct)
        sign = "+" if alpha >= 0 else ""
        return (
            f"S&P 500 (SPY)   : {self.return_pct:+.2f}%  (${self.current_value:,.2f})\n"
            f"Portfolio       : {portfolio_return_pct:+.2f}%\n"
            f"Alpha           : {sign}{alpha:.2f} pp  {'BEATING' if alpha > 0 else 'TRAILING'} the benchmark"
        )
