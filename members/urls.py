from django.contrib import admin
from django.urls import path
from members import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.index, name='members'),
    path("index", views.index, name='index'),
    path("contact", views.contact, name='contact'),
    path("Admission", views.Admission, name='Admission'),
    # path("Admission", login_required(views.Admission), name='Admission'),
    path("contact",views.view_subject),
    path("Next", views.Next, name='Next'),

    path("storedata/",views.storedata),
    path("view_details/",views.view_subject,name='view_subject'),
    path("Icard/<str:id>/",views.Icard),
    path('deletedata/',views.deletedata,name='deletedata'),
    path('editdata/',views.editdata,name='editdata'),
    path('approval/',views.approval,name='approval'),
    path('updatedata/',views.updatedata,name="updatedata"),

    path('mca/',views.mca),
    path('bca/',views.bca),
    path('mba/',views.mba),
    path('degree/',views.degree),
    path('sf/',views.sf),

    
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout',views.signout, name="signout"),
    path('activate/<uid64>/<token>',views.activate, name="activate"),

]
