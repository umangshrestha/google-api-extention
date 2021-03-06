from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.shortcuts import redirect
from .views import *


urlpatterns = [
    path(r'auth/', AuthList.as_view()),
    path(r'url/', UrlList.as_view()),
    path(r'status/', StatusList.as_view()),
    path(r'auth/<int:pk>', AuthDetail.as_view()),
    path(r'url/<int:pk>', UrlDetail.as_view()),
    # upload urls
    path(r'api/url/', UrlPost.as_view()),
    path(r'api/auth/', AuthPost.as_view()),
    path(r'api/upload/', DataPost.as_view()),
    # get data
    path(r'api/data/success/', SuccessData.as_view()),
    path(r'api/data/failure/', FailedData.as_view()),

    path(r'api/data/', GetData.as_view()),
   path(r'status/<int:pk>', StatusDetail.as_view()),
]
