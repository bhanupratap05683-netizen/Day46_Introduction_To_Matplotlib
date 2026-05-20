"""
Day 46 - Introduction to matplotlib
Topic: Line, Bar, Scatter, Histogram charts using real financial data
File: Day46_Matplotlib_Intro.py
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

# ─── LOAD DATA ────────────────────────────────────────────────────────────────
FILE = "Day46_Matplotlib_Practice.xlsx"

df_stocks  = pd.read_excel(FILE, sheet_name="Stock_Prices")
df_revenue = pd.read_excel(FILE, sheet_name="Monthly_Revenue")
df_scatter = pd.read_excel(FILE, sheet_name="Portfolio_Returns")
df_hist    = pd.read_excel(FILE, sheet_name="Daily_Returns")

print("Data loaded successfully.")
print(f"  Stock_Prices      : {df_stocks.shape}")
print(f"  Monthly_Revenue   : {df_revenue.shape}")
print(f"  Portfolio_Returns : {df_scatter.shape}")
print(f"  Daily_Returns     : {df_hist.shape}")


# ═══════════════════════════════════════════════════════════════════════════════
# CHART 1 — LINE CHART
# Shows stock price movement over time for 4 stocks.
# ═══════════════════════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(12, 5))      # figsize = (width, height) in inches

# Plot one line per stock
ax.plot(df_stocks["Date"], df_stocks["RELIANCE"], marker="o", label="RELIANCE", color="#1F77B4", linewidth=2)
ax.plot(df_stocks["Date"], df_stocks["TCS"],      marker="s", label="TCS",      color="#FF7F0E", linewidth=2)
ax.plot(df_stocks["Date"], df_stocks["INFY"],     marker="^", label="INFY",     color="#2CA02C", linewidth=2)
ax.plot(df_stocks["Date"], df_stocks["HDFC"],     marker="D", label="HDFC",     color="#D62728", linewidth=2)

# Labels & title
ax.set_title("Stock Price Movement — FY 2024", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Month",       fontsize=11)
ax.set_ylabel("Price (₹)",   fontsize=11)
ax.legend(loc="upper left",  fontsize=10)
ax.grid(True, linestyle="--", alpha=0.5)          # grid makes reading easier
plt.xticks(rotation=45, ha="right")               # rotate x-axis labels
plt.tight_layout()                                 # auto-fix spacing
plt.savefig("Day46_Chart1_Line.png", dpi=150)
plt.show()
print("Chart 1 (Line) saved.")


# ═══════════════════════════════════════════════════════════════════════════════
# CHART 2 — BAR CHART
# Compares Revenue vs Expenses month by month.
# ═══════════════════════════════════════════════════════════════════════════════

import numpy as np

months   = df_revenue["Month"]
revenue  = df_revenue["Revenue (₹ Lakh)"]
expenses = df_revenue["Expenses (₹ Lakh)"]

x      = np.arange(len(months))   # [0, 1, 2, ... 11] — positions for bars
width  = 0.35                      # width of each bar

fig, ax = plt.subplots(figsize=(13, 5))

bars1 = ax.bar(x - width/2, revenue,  width, label="Revenue",  color="#2196F3", alpha=0.85)
bars2 = ax.bar(x + width/2, expenses, width, label="Expenses", color="#F44336", alpha=0.85)

# Add value labels on top of each bar
ax.bar_label(bars1, fmt="%.1f", fontsize=8, padding=2)
ax.bar_label(bars2, fmt="%.1f", fontsize=8, padding=2)

ax.set_title("Monthly Revenue vs Expenses (₹ Lakh)", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Month",          fontsize=11)
ax.set_ylabel("Amount (₹ Lakh)", fontsize=11)
ax.set_xticks(x)
ax.set_xticklabels(months, rotation=45, ha="right")
ax.legend(fontsize=10)
ax.grid(True, axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("Day46_Chart2_Bar.png", dpi=150)
plt.show()
print("Chart 2 (Bar) saved.")


# ═══════════════════════════════════════════════════════════════════════════════
# CHART 3 — SCATTER CHART
# Risk vs Return for each stock. Classic finance visualization.
# ═══════════════════════════════════════════════════════════════════════════════

fig, ax = plt.subplots(figsize=(9, 6))

risk    = df_scatter["Risk (%)"]
returns = df_scatter["Return (%)"]
invest  = df_scatter["Investment (₹ Lakh)"]
names   = df_scatter["Stock"]

# Size of dot = size of investment (scaled)
scatter = ax.scatter(risk, returns, s=invest*40, c=returns,
                     cmap="RdYlGn", alpha=0.75, edgecolors="grey", linewidth=0.8)

# Label each dot with stock name
for i, name in enumerate(names):
    ax.annotate(name, (risk.iloc[i], returns.iloc[i]),
                textcoords="offset points", xytext=(5, 5), fontsize=8)

cbar = plt.colorbar(scatter, ax=ax)
cbar.set_label("Return (%)", fontsize=10)

ax.set_title("Risk vs Return — Portfolio Stocks", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Risk / Volatility (%)", fontsize=11)
ax.set_ylabel("Annual Return (%)",     fontsize=11)
ax.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("Day46_Chart3_Scatter.png", dpi=150)
plt.show()
print("Chart 3 (Scatter) saved.")


# ═══════════════════════════════════════════════════════════════════════════════
# CHART 4 — HISTOGRAM
# Distribution of daily returns. Core concept in risk management.
# ═══════════════════════════════════════════════════════════════════════════════

daily_ret = df_hist["Daily Return (%)"]

fig, ax = plt.subplots(figsize=(9, 5))

ax.hist(daily_ret, bins=30, color="#5C6BC0", edgecolor="white",
        alpha=0.85, density=False)

# Mark mean and std lines
mean_val = daily_ret.mean()
std_val  = daily_ret.std()

ax.axvline(mean_val,             color="red",    linestyle="--", linewidth=1.8, label=f"Mean: {mean_val:.2f}%")
ax.axvline(mean_val + std_val,   color="orange", linestyle="--", linewidth=1.4, label=f"+1 SD: {mean_val+std_val:.2f}%")
ax.axvline(mean_val - std_val,   color="orange", linestyle="--", linewidth=1.4, label=f"-1 SD: {mean_val-std_val:.2f}%")

ax.set_title("Distribution of Daily Returns — 252 Trading Days", fontsize=14, fontweight="bold", pad=15)
ax.set_xlabel("Daily Return (%)", fontsize=11)
ax.set_ylabel("Frequency",        fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig("Day46_Chart4_Histogram.png", dpi=150)
plt.show()
print("Chart 4 (Histogram) saved.")


# ═══════════════════════════════════════════════════════════════════════════════
# BONUS — ALL 4 CHARTS IN ONE FIGURE (subplot grid)
# This is what you'll use in portfolio reports.
# ═══════════════════════════════════════════════════════════════════════════════

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle("Financial Analysis Dashboard — Day 46", fontsize=16, fontweight="bold", y=1.01)

# --- Top-left: Line ---
ax = axes[0, 0]
for col, color in zip(["RELIANCE","TCS","INFY","HDFC"], ["#1F77B4","#FF7F0E","#2CA02C","#D62728"]):
    ax.plot(df_stocks["Date"], df_stocks[col], marker="o", label=col, color=color, linewidth=1.8, markersize=4)
ax.set_title("Stock Prices — FY 2024")
ax.legend(fontsize=8)
ax.tick_params(axis="x", rotation=45)
ax.grid(True, linestyle="--", alpha=0.4)

# --- Top-right: Bar ---
ax = axes[0, 1]
ax.bar(x - width/2, revenue,  width, label="Revenue",  color="#2196F3", alpha=0.85)
ax.bar(x + width/2, expenses, width, label="Expenses", color="#F44336", alpha=0.85)
ax.set_title("Revenue vs Expenses (₹ Lakh)")
ax.set_xticks(x)
ax.set_xticklabels(months, rotation=45, ha="right", fontsize=7)
ax.legend(fontsize=8)
ax.grid(True, axis="y", linestyle="--", alpha=0.4)

# --- Bottom-left: Scatter ---
ax = axes[1, 0]
sc = ax.scatter(risk, returns, s=invest*30, c=returns, cmap="RdYlGn", alpha=0.75, edgecolors="grey")
for i, name in enumerate(names):
    ax.annotate(name, (risk.iloc[i], returns.iloc[i]), textcoords="offset points", xytext=(4,4), fontsize=7)
ax.set_title("Risk vs Return")
ax.grid(True, linestyle="--", alpha=0.4)

# --- Bottom-right: Histogram ---
ax = axes[1, 1]
ax.hist(daily_ret, bins=30, color="#5C6BC0", edgecolor="white", alpha=0.85)
ax.axvline(mean_val, color="red", linestyle="--", linewidth=1.8, label=f"Mean: {mean_val:.2f}%")
ax.set_title("Daily Returns Distribution")
ax.legend(fontsize=8)
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout()
plt.savefig("Day46_Chart5_Dashboard.png", dpi=150, bbox_inches="tight")
plt.show()
print("\nAll 5 charts saved. Day 46 complete!")
