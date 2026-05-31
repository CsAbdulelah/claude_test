"""
Portfolio strategy: $1000 challenge to beat S&P 500.

Approach: Concentrated momentum + quality factor tilt.
Core thesis — own fewer, higher-conviction positions in secular
growth themes where earnings revisions are positive and technicals confirm.
Rebalance monthly; cut losers at -15%, let winners run.
"""

from dataclasses import dataclass, field
from datetime import date
from typing import Optional


@dataclass
class Position:
    ticker: str
    shares: float
    avg_cost: float          # cost basis per share
    current_price: float
    sector: str
    thesis: str

    @property
    def market_value(self) -> float:
        return self.shares * self.current_price

    @property
    def cost_basis(self) -> float:
        return self.shares * self.avg_cost

    @property
    def unrealized_pnl(self) -> float:
        return self.market_value - self.cost_basis

    @property
    def pnl_pct(self) -> float:
        return (self.current_price - self.avg_cost) / self.avg_cost * 100


@dataclass
class Portfolio:
    start_date: date
    starting_cash: float = 1000.0
    cash: float = field(init=False)
    positions: dict[str, Position] = field(default_factory=dict)
    realized_pnl: float = 0.0
    transaction_log: list[dict] = field(default_factory=list)

    def __post_init__(self):
        self.cash = self.starting_cash

    @property
    def total_value(self) -> float:
        return self.cash + sum(p.market_value for p in self.positions.values())

    @property
    def total_return_pct(self) -> float:
        return (self.total_value - self.starting_cash) / self.starting_cash * 100

    def buy(self, ticker: str, shares: float, price: float, sector: str, thesis: str) -> None:
        cost = shares * price
        if cost > self.cash:
            raise ValueError(f"Insufficient cash: need ${cost:.2f}, have ${self.cash:.2f}")

        if ticker in self.positions:
            pos = self.positions[ticker]
            total_shares = pos.shares + shares
            pos.avg_cost = (pos.cost_basis + cost) / total_shares
            pos.shares = total_shares
            pos.current_price = price
        else:
            self.positions[ticker] = Position(ticker, shares, price, price, sector, thesis)

        self.cash -= cost
        self.transaction_log.append({
            "date": date.today().isoformat(),
            "action": "BUY",
            "ticker": ticker,
            "shares": shares,
            "price": price,
            "value": cost,
        })

    def sell(self, ticker: str, shares: Optional[float] = None) -> None:
        if ticker not in self.positions:
            raise ValueError(f"{ticker} not in portfolio")

        pos = self.positions[ticker]
        shares = shares or pos.shares
        proceeds = shares * pos.current_price
        pnl = (pos.current_price - pos.avg_cost) * shares

        self.cash += proceeds
        self.realized_pnl += pnl
        self.transaction_log.append({
            "date": date.today().isoformat(),
            "action": "SELL",
            "ticker": ticker,
            "shares": shares,
            "price": pos.current_price,
            "value": proceeds,
            "pnl": pnl,
        })

        if shares >= pos.shares:
            del self.positions[ticker]
        else:
            pos.shares -= shares

    def update_price(self, ticker: str, price: float) -> None:
        if ticker in self.positions:
            self.positions[ticker].current_price = price

    def check_stop_losses(self, stop_pct: float = -15.0) -> list[str]:
        """Return tickers that have breached the stop-loss threshold."""
        return [t for t, p in self.positions.items() if p.pnl_pct <= stop_pct]

    def summary(self) -> str:
        lines = [
            f"Portfolio Value : ${self.total_value:,.2f}",
            f"Cash            : ${self.cash:,.2f}",
            f"Total Return    : {self.total_return_pct:+.2f}%",
            f"Realized P&L    : ${self.realized_pnl:+,.2f}",
            "",
            f"{'Ticker':<6}  {'Shares':>7}  {'Cost':>8}  {'Price':>8}  {'Value':>9}  {'P&L':>9}  {'%':>7}  Sector",
            "-" * 80,
        ]
        for pos in sorted(self.positions.values(), key=lambda p: -p.market_value):
            lines.append(
                f"{pos.ticker:<6}  {pos.shares:>7.3f}  ${pos.avg_cost:>7.2f}  "
                f"${pos.current_price:>7.2f}  ${pos.market_value:>8.2f}  "
                f"${pos.unrealized_pnl:>+8.2f}  {pos.pnl_pct:>+6.1f}%  {pos.sector}"
            )
        return "\n".join(lines)
