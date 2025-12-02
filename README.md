# Binance Futures Order Bot — CLI Trading System

Developer: **Bhaskara Sri Vaishnavi**  
Mode: **Binance USDT-M Futures Testnet** (Safe / Virtual Funds)

## 🔹 Project Overview

This project is a fully functional **CLI-based trading bot** for **Binance USDT-M Futures**, designed with:

- Automated order execution  
- Modular architecture  
- Safe Testnet environment  
- Support for advanced strategies  

The bot supports **market**, **limit**, **stop-limit**, **OCO**, **TWAP**, and **Grid** strategies.  
All actions are logged to **bot.log**.

## 🔹 Features

| Feature | Status |
|--------|--------|
| Market Orders | ✔ |
| Limit Orders | ✔ |
| Stop-Limit Orders | ✔ |
| OCO Orders | ✔ |
| TWAP Strategy | ✔ |
| Grid Strategy | ✔ |
| Logging System | ✔ |
| CLI Interface | ✔ |
| Testnet Safe Mode | ✔ |

## 🔹 Folder Structure

```
binance_bot/
│
├── src/
│   ├── main.py
│   ├── client.py
│   ├── logger.py
│   ├── validator.py
│   ├── market_orders.py
│   ├── limit_orders.py
│   ├── advanced/
│       ├── stop_limit.py
│       ├── oco.py
│       ├── twap.py
│       ├── grid_strategy.py
│
├── bot.log
├── README.md
├── report.pdf
└── .env
```

## 🔹 Setup Instructions

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
```

### 2️⃣ Activate Environment

**Windows**
```bash
.\.venv\Scripts\activate
```

**Linux / WSL**
```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install python-binance rich python-dotenv requests
```

### 4️⃣ Add Testnet Keys in `.env`
```
BINANCE_API_KEY=your_key_here
BINANCE_API_SECRET=your_secret_here
```

## 🔹 How to Run CLI Commands

### Syntax
```bash
python src/main.py <ORDER_TYPE> <SYMBOL> <SIDE> <QUANTITY>
```

### Examples

| Feature | Command |
|--------|---------|
| Market | `python src/main.py MARKET ETHUSDT BUY 0.01` |
| Limit | `python src/main.py LIMIT ETHUSDT BUY 0.01` |
| Stop-Limit | `python src/main.py STOP-LIMIT ETHUSDT BUY 0.01` |
| OCO | `python src/main.py OCO ETHUSDT BUY 0.01` |
| TWAP | `python src/main.py TWAP ETHUSDT BUY 0.05` |
| Grid | `python src/main.py GRID ETHUSDT BUY 0.05` |

## 🔹 Logging

- Order placements  
- Errors  
- Strategy execution  
- Timestamps  

Saved in `bot.log`.

## 🔹 Disclaimer

Testnet only.  
No real funds.  
Zero financial risk.

## 🔹 Future Improvements

- Docker support  
- UI Dashboard  
- Smart Grid  
- Risk Controls
