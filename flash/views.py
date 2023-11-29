from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.utils import timezone
import random
import requests
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
class HomePage(TemplateView):
    template_name = "home.html"

class WhoWeArePage(TemplateView):
    template_name = "who-we-are.html"

class BoardPage(TemplateView):
    template_name = "board-directores.html"

class FundTypePage(TemplateView):
    template_name = "fund-type.html"

class OneRpsPage(TemplateView):
    template_name = "one-rps.html"

class OneEtfPage(TemplateView):
    template_name = "one-etf.html"

class AltInvestPage(TemplateView):
    template_name = "alt-invest.html"

class CoporatePage(TemplateView):
    template_name = "coporate-services.html"

class WealthPage(TemplateView):
    template_name = "private-wealth.html"

class PlanningPage(TemplateView):
    template_name = "financial-planning.html"

class EPFPage(TemplateView):
    template_name = "epf-member.html"

class WealthManagementPage(TemplateView):
    template_name = "wealth-management.html"



def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = 'Ascente Contact Support Form'
            message = f"CL Name: {form.cleaned_data['name']}\n CL Email: {form.cleaned_data['email']}\n\n{form.cleaned_data['message']}"
            sender = 'jamescord40@gmail.com'
            recipient = ['ascenteinvestmentgroup@gmail.com']

            send_mail(subject, message, sender, recipient)

            messages.success(request, 'Email sent successfully!')
            return redirect('home') 
        else:
            messages.error(request, 'Failed to send email. Please correct the form errors.')
            return redirect('speak') 

         # Redirect back to the form page
    else:
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})


def unit_fund_view(request, *args, **kwargs):
    fund_names = [
        ["Ascenet Amanah Saham Wanita", "Conventional-Local", "Equity", "Growth", "0.3485"],
        ["Ascenet TacticalEXTRA Fund", "Conventional-Local", "Equity", "Growth", "0.6356"],
        ["Ascenet Balanced Fund", "Conventional-Local", "Balanced", "Growth & Income", "0.8356"],
        ["Ascenet SyariahEXTRA Fund", "Shariah-Local", "Balanced", "Growth and to a lesser extent income.", "0.3456"],
        ["Ascenet MoneyEXTRA Fund", "Conventional-Local", "Fixed Income", "Income", "0.5769"],
        ["Ascenet Bond Fund", "Conventional-Local", "Fixed Income", "Income", "0.6583"],
        ["Ascenet Global Unicorn 2 (MYR)", "Conventional-Global", "Equity (Feeder)", "Growth (closed-end)", "0.5751"],
        ["Ascenet AUD Alternative Income Fund 3 (AUD)", "Conventional-Global", "Mixed Assets (Feeder)", "Growth & Income", "0.2088"],
        ["Ascenet OnePRS Growth Fund", "Conventional", "Core Fund", "Growth", "0.7088"],
        ["Ascenet OnePRS Shariah Equity Fund", "Shariah", "Non-Core Fund", "Feeder (Equity)", "0.5872"],
        ["Ascenet OnePRS Moderate Fund", "Conventional", "Core Fund", "Moderate", "0.7033"],
        ["Ascenet US Dollar Fund", "Conventional-Global", "Money Market (Feeder)", "Income", "1.0002"],
        ["Ascenet ASnitaBOND Fund", "Shariah-Local", "Bond (Sukuk)", "Income", "1.0000"],
        ]

    # Generate a list of funds with accurate dates and random values for the provided names
    funds = []
    for fund_name in fund_names:
        fund = {
            'name': fund_name[0],
            'class': fund_name[1],
            'cat': fund_name[2],
            'type': fund_name[3],
            'nav': fund_name[4],
            'date': timezone.now().strftime('%Y-%m-%d'),
            'value': round(random.uniform(-10, 10), 2),  # Random float between -10 and 10
        }
        funds.append(fund)

    # Render the HTML template with the funds data
    return render(request, 'fund-listing.html', {'funds': funds})

def blog_view(request, *args, **kwargs):
    # News API endpoint and API key (replace 'YOUR_API_KEY' with your actual API key)
    api_url = 'https://newsapi.org/v2/everything'
    api_key = 'a9d93e4a6d37494bb83f4be2ce3a065c'

    # Specify the parameters for the API request
    params = {
        'q': "finance",
        'apiKey': api_key,
    }

    # Make the API request
    response = requests.get(api_url, params=params)
    news_data = response.json()
    articles = news_data.get('articles', [])
    return render(request, 'list-blog.html', {'funds': articles})
