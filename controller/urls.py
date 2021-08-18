from django.urls import path
from . import views
from .views import PostListView,PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
<<<<<<< HEAD
      path('', views.home, name='controller-home'),
      path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
      path('post/new', PostCreateView.as_view(), name='post-create'),
      path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
      path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
      path('about/', PostListView.as_view(), name='controller-about'),
=======
    
    path('', views.home, name='controller-home'),
    path('about/', views.about, name='controller-about'),
    
    
>>>>>>> a7d36c52cbf72f2b9d0bfb9ec0b0f8e1d3c33e8f

]
