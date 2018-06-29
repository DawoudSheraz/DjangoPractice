from django.conf.urls import url
from . import views


app_name = "user_profiling"
urlpatterns = [
    url(r'^$', views.IndexView, name="index"),
    url(r'^add/$', views.addView, name="add"),
    url(r'^save/$', views.SaveView, name="save"),
    url(r'^search/$', views.SearchView, name="search"),
    url(r'^edit/$', views.EditView, name="edit"),
    url(r'^editSave/$', views.EditSave, name="editSave"),
    url(r'^searchReadOnlyInput/$', views.searchReadOnlyInputView, name="searchReadOnly"),
    url(r'^viewData/$', views.DataView, name="view_search"),
    url(r'^deleteDataInput/$', views.deleteInput, name="deleteInput"),
    url(r'^delete/$', views.deleteData, name="delete"),



]
