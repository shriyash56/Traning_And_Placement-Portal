"""tnp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from basic_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home.as_view(),name='home'),
    path('register/',views.register,name='register'),
    path('logout/',views.user_logout,name='logout'),
    path('userlogin/',views.user_login,name='user_login'),
    path('student/',views.student_info,name='student_info'),
    path('show/',views.show,name='show'),
    path('map/',views.map,name='map'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
    path('sort/',views.sort,name='sort'),
    path('mplimage/',views.mplimage,name='mplimage'),
    path('search/',views.search,name='search'),
    path('pstudent/',views.pstudent,name='pstudent'),
    path('searchcompany/',views.searchcompany,name="searchcompany"),
    path('per_delete/<int:id>',views.per_delete,name='per_delete'),
    path('pedit/<int:id>',views.pedit,name='pedit'),
    path('pupdate/<int:id>', views.pupdate, name='pupdate'),
    path('p_per_delete/<int:id>', views.p_per_delete, name='p_per_delete'),
    path('email/',views.email,name='email'),
    path('data_csv/',views.data_csv,name='data_csv'),
    path('data_csv1/',views.data_csv1,name='data_csv1'),
]
