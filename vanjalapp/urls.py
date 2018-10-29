from django.urls import path
from . import views
urlpatterns = [
	path('index/',views.index,name='index'),
	path('index/login/',views.login,name='login'),
	path('index/signup/',views.register,name='register'),
	path('index/loginIndex/',views.loginIndex,name='loginIndex'),
	path('index/login/about/',views.about,name='about'),
	path('index/trees',views.trees,name='trees'),
	path('index/water',views.water,name='water'),
	path('index/air',views.air,name='air'),
	path('index/error',views.error,name='error'),
	path('index/addAboutPage',views.addAboutPage,name='addAboutPage'),
	path('index/complaints',views.complaints,name='complaints'),
	path('index/govLogin',views.govLogin,name='govLogin'),
	path('index/getcomplaints',views.getcomplaints,name='getcomplaints'),
	path('index/user',views.user,name='user'),
]