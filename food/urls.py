from django import views
from django.urls import path
from .views import CreateItem, index, item , detail , create_item , update_item , delete_item


app_name = 'food'# this called namespacing and its agood practice in big scalle applications
urlpatterns = [
    path('', index , name="index" ),
    path('item/', item, name='item'),
    path('<int:item_id>/' ,detail, name='detail'),
    # path('add/', create_item, name='create_item' ),
    # CBV
    path('add/', CreateItem.as_view() , name='create_item' ),
    
    
    path('update/<int:id>/', update_item , name= "update_item"),
    #delete
    path('delete/<int:id>/', delete_item, name= 'delete_item')
]
