from django.conf.urls import url
from views import index,add
urlpatterns = [
    url('index',index,name="index"),
    url('add',add,name="add"),
]
