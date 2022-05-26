from django.urls import URLPattern, path,re_path

from . import views


urlpatterns=[
    re_path(r'^mult/(\w+)/$',views.mult),
    re_path(r'^search/',views.search_results,name="search_results"),
    path('add/',views.add_teacher,name="add_teacher"),
    path('real/',views.other)
]