# Stock_analysis_AI# Stock Analysis AI

A full-stack web application for stock market analysis that provides price visualization, technical indicators, and basic trading signals.

---
## Overview

This project is designed to analyze stock market data and present insights through a modern web interface. It integrates a Python-based backend for data processing and a React-based frontend for visualization.

---

## Features

* Fetch historical stock price data
* Visualize price trends
* Compute moving averages (MA50, MA200)
* Generate basic buy/sell signals
* Modular full-stack architecture

---

## Tech Stack

**Frontend**

* React (Vite)
* TypeScript

**Backend**

* FastAPI (Python)
* yFinance
* Pandas
* Matplotlib

---

## Project Structure

```id="p6o8mb"
Stock_analysis_AI/
├── frontend/
├── backend/
├── .gitignore
└── README.md
```

---

## Getting Started

### Clone the repository

```id="3tx2fr"
git clone https://github.com/DKS-2020/Stock_analysis_AI.git
cd Stock_analysis_AI
```

### Backend setup

```id="d6k6kn"
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### Frontend setup

```id="3tx1yd"
cd frontend
npm install
npm run dev
```

---

## Usage

* Frontend: http://localhost:5173
* Backend: http://127.0.0.1:8000

---

## Environment Variables

Create a `.env` file in the backend directory:

```id="mb9l86"
API_KEY=your_api_key_here
```

Ensure `.env` is excluded from version control.

---
## Future Work
* Integration of additional technical indicators (RSI, MACD)
* AI-based prediction models
* Real-time data streaming
* Interactive dashboard improvements

---

## License

This project is licensed under the MIT License.

---

## Author

Deepak
https://github.com/DKS-2020
