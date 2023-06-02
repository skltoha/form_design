from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.userHome, name="user-home"),
    path('form/', v.userform, name="user-form"),
    path('store/', v.userStore, name="user-store"),
    path('record/', v.userRecord, name="user-record"),
]
