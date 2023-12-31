from django.urls import path
from .views import (
    HomePage, WhoWeArePage, BoardPage, FundTypePage, OneRpsPage, OneEtfPage, AltInvestPage,
    CoporatePage, WealthPage, WealthManagementPage ,PlanningPage, EPFPage,
    send_email, unit_fund_view,
    )

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("we", WhoWeArePage.as_view(), name="we"),
    path("structure", HomePage.as_view(), name="structure"),
    path("board", BoardPage.as_view(), name="board"),
    path("management-team", HomePage.as_view(), name="management-team"),
    path("book", HomePage.as_view(), name="book"),
    path("speak", send_email, name="speak"),
    path("office", HomePage.as_view(), name="office"),
    path("register", HomePage.as_view(), name="register"),
    # path("sign-in", HomePage.as_view(), name="sign-in"),
    path("about", HomePage.as_view(), name="about"),
    path("mission", HomePage.as_view(), name="mission"),
    path("philosophy", HomePage.as_view(), name="philosophy"),
    path("partner", HomePage.as_view(), name="partner"),
    path("awards", HomePage.as_view(), name="awards"),
    path("fund", FundTypePage.as_view(), name="fund"),
    path("one-rps", OneRpsPage.as_view(), name="one-rps"),
    path("one-etf", OneEtfPage.as_view(), name="one-etf"),
    path("unit-funds", unit_fund_view, name="unit-fund"),
    path("funds-list", unit_fund_view, name="list-funds"),
    path("alt-invest", AltInvestPage.as_view(), name="alt-invest"),
    path("coporate", CoporatePage.as_view(), name="coporate"),
    path("private-wealth", WealthPage.as_view(), name="wealth"),
    path("financial-planning", PlanningPage.as_view(), name="planning"),
    path("epf-member", EPFPage.as_view(), name="member"),
    path("wealth-management", WealthManagementPage.as_view(), name="wealth-man"),
]