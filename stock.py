import yfinance as yf


def track_stocks(tickers):
    with open('stocks.html', 'w') as f:
        f.write("""
        <html>
            <head>
                <style>
                    table {
                        font-family: arial, sans-serif;
                        border-collapse: collapse;
                        width: 100%;
                    }

                    td, th {
                        border: 1px solid #dddddd;
                        text-align: left;
                        padding: 8px;
                    }

                    tr:nth-child(even) {
                        background-color: #dddddd;
                    }
                </style>
            </head>
            <body>""")

        for ticker in tickers:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="1d")
            data = hist.to_html()

            f.write(f"<h2>{ticker}</h2>")
            f.write(data)

        f.write("""
            </body>
        </html>""")


track_stocks(["AAPL", "MSFT"])  # Example: tracking Apple Inc. and Microsoft Corporation stocks