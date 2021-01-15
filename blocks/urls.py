from django.urls import path
from . import views

urlpatterns = [
    path('blocks', views.blocks, name='blocks'),
    path('blocks/<int:pk>', views.detail_block, name='block_height')
]
