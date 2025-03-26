from django.urls import path,include
from . import views
from .views import authView,home,logout_view
from django.contrib.auth.views import LogoutView

app_name="TradeSen"

urlpatterns = [
   path("",home,name="home"),
   path("signup/",authView,name="signup"),
   path("accounts/",include("django.contrib.auth.urls")),
   path("logout/", logout_view, name="logout"),
   path('market-summary/', views.market_summary, name='market_summary'),
]

