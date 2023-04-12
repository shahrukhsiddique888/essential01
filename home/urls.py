from django.urls import path
from . import views

urlpatterns = [
    path('',views.ModelView.as_view() ),
    path('d/',views.ModelListView.as_view(), name='hell'),
    path('d/<int:pk>', views.ModelDetailView.as_view(), name='he')
]
