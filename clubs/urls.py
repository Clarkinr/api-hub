from django.urls import path
from clubs import views


urlpatterns = [
    path('clubs/', views.ClubList.as_view()),
    path('clubs/<int:pk>', views.ClubDetail.as_view())
]
