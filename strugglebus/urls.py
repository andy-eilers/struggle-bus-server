from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from strugglebusapi.views import register_user, login_user, BusView, RiderView, PostView, StruggleView
from rest_framework import routers
from django.contrib import admin
from django.urls import path

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'busses', BusView, 'bus')
router.register(r'posts', PostView, 'post')
router.register(r'riders', RiderView, 'rider')
router.register(r'struggles', StruggleView, 'struggle')

urlpatterns = [
    path('register', register_user),
    path('login', login_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]