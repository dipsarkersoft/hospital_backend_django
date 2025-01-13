from rest_framework.routers import DefaultRouter
from django.urls import path,include
from .views import PatientViewset,RegisterViewset,activate,UserLoginView,UserLogOutView


router=DefaultRouter()

router.register('list',PatientViewset)

urlpatterns = [
    path('',include(router.urls)),
    path('register/',RegisterViewset.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogOutView.as_view(),name='logout'),
    path('active/<uid64>/<token>',activate,name='activeuser')
]

