# Day 46 — Introduction to matplotlib

**Phase 3 | Data Cleaning & Processing**
**Date:** May 20, 2026
**Topic:** Basic charts with matplotlib — Line, Bar, Scatter, Histogram

---

## Overview

Introduced matplotlib for financial data visualization. Built 4 chart types using real market data and combined them into a single dashboard subplot layout.

---

## Files

| File | Description |
|------|-------------|
| `Day46_Matplotlib_Practice.xlsx` | Input data — 4 sheets: Stock Prices, Revenue, Portfolio, Daily Returns |
| `Day46_Matplotlib_Intro.py` | Full practice script — 4 charts + dashboard |
| `Day46_Chart1_Line.png` | Stock price line chart |
| `Day46_Chart2_Bar.png` | Revenue vs Expenses bar chart |
| `Day46_Chart3_Scatter.png` | Risk vs Return scatter plot |
| `Day46_Chart4_Histogram.png` | Daily returns distribution |
| `Day46_Chart5_Dashboard.png` | 2×2 subplot dashboard (all 4 charts) |

---

## Key Concepts Learned

- `plt.subplots()` — figure and axes creation
- `ax.plot()` — line charts with markers
- `ax.bar()` — grouped bar charts with `np.arange()` positioning
- `ax.scatter()` — scatter plots with size and color encoding
- `ax.hist()` — frequency distribution with bin control
- `ax.axvline()` — reference lines (mean, std deviation)
- `plt.tight_layout()` — auto-fix spacing
- `plt.savefig()` — export charts as PNG
- Subplots grid with `plt.subplots(2, 2)`

---

## Portfolio Connection

Chart output feeds directly into:
- **Phase 3 (Day 49):** Visual Report Generation — embedding charts in PDF reports
- **Phase 7 (Day 78):** Financial Dashboard project — live data + xlwings + matplotlib

---

## Skills Stack Progress

`Python` → `openpyxl` → `pandas` → **`matplotlib`** → `xlwings` → `APIs` → Portfolio
