from django.urls import path
from .views import send_document, receive_document, dashboard, add_user

app_name="staffs"

urlpatterns = [
    path("send/", send_document, name="send-document"),
    path("receive/", receive_document, name="receive-document"),
    path("dashboard/", dashboard, name="dashboard"),
    path("add_user/", add_user, name="add-user")
]