from django.urls import path, include
from email_app.views import lgsp_email, all_pnr_list, add_pnr, login_page, log_out, add_priority, view_priority

urlpatterns = [
    
    
    path('', login_page, name="login"),
    path('view_email/', all_pnr_list, name="view_email"),
    path('email/<str:pnr>/', lgsp_email, name="lgsp_email"),
    path('add_pnr/', add_pnr, name="add_pnr"),
    path('add_priority/', add_priority, name="add_priority"),
    path('view_priority/', view_priority, name="view_priority"),

    path('log_out/', log_out, name='log_out'),
   
    
]

