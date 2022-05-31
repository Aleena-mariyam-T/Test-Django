from django.urls import path
from .import views
urlpatterns=[
    # path('',MytemplateView.as_view(template_name="app/index.html")),
    path('',views.MytemplateView.as_view(),name="MytemplateView"),
    path('user_login/',views.user_login,name="user_login"),
    path('event/',views.event,name="event"),
    path('CreateCheckoutSession',views.CreateCheckoutSession.as_view(),name="CreateCheckoutSession"),
]