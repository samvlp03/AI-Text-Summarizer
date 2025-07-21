from django.contrib import admin
from django.urls import path
from summarizer.views import (
    SummarizeView, RegenerateView, UpdateSummaryView,
    ToggleFavoriteView, SummaryListView, ExportSummaryView,
    ExportFormatListView, MyTokenObtainPairView, UserCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/register/', UserCreateView.as_view(), name='register'),
    path('api/auth/login/', MyTokenObtainPairView.as_view(), name='login'),
    path('api/summarize/', SummarizeView.as_view(), name='summarize'),
    path('api/summarize/<int:summary_id>/regenerate/', RegenerateView.as_view(), name='regenerate'),
    path('api/summarize/<int:summary_id>/update/', UpdateSummaryView.as_view(), name='update-summary'),
    path('api/summarize/<int:summary_id>/favorite/', ToggleFavoriteView.as_view(), name='toggle-favorite'),
    path('api/summarize/list/', SummaryListView.as_view(), name='summary-list'),
    path('api/summarize/<int:summary_id>/export/', ExportSummaryView.as_view(), name='export-summary'),
    path('api/export-formats/', ExportFormatListView.as_view(), name='export-formats'),
]