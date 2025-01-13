from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views


router=DefaultRouter()

router.register('list',views.DoctorViewset)
router.register('availabletime',views.AvailableTimeViewset)
router.register('designation',views.DesigationViewset)
router.register('speacalization',views.SpeacializationViewset)
router.register('review',views.ReviewViewset)

urlpatterns = [
    path('',include(router.urls))
]

