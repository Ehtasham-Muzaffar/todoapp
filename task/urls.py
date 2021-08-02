from django.urls import path
from task import views

urlpatterns = [
path('',views.index,name="index"),    
path('show',views.show,name="show"),
path('delete/<int:id>',views.delete,name='delete'),    
path('edit/<int:id>',views.edit,name='edit'),    
path('update/<int:id>',views.updates,name='update')   

]

