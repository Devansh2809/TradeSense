from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
# views.py
import requests
from django.shortcuts import render

def market_summary(request):
    # Example using yfinance for stock data
    import yfinance as yf

    # List of stock symbols to display
    stocks = ["AAPL", "AMD", "AMZN", "IWM", "META", "QQQ", "SPY", "TSLA", "UBER"]
    stock_data = []

    for symbol in stocks:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1d")  # Get today's data
        price = hist['Close'].iloc[-1] if not hist.empty else 0
        change = hist['Close'].iloc[-1] - hist['Open'].iloc[-1] if not hist.empty else 0
        percent_change = (change / hist['Open'].iloc[-1]) * 100 if not hist.empty else 0

        stock_data.append({
            "symbol": symbol,
            "price": round(price, 2),
            "change": round(change, 2),
            "percent_change": f"{round(percent_change, 2)}%"
        })

    context = {"stock_data": stock_data}
    return render(request, 'market_summary.html', context)


# Home View
@login_required
def home(request):
    return render(request, "home.html", {})

# Signup View
def authView(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home') 
    else:
        form = UserCreationForm()
    return render(request, "registration/signup.html", {"form": form})

def logout_view(request):
    logout(request)
    return redirect('TradeSen:login')  
