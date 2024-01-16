from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upload/',views.upload, name='upload'),
    path('insert1/',views.insert1,name='insert1'),
    path('insert2/',views.insert2,name='insert2'),
    path('comment/',views.comment,name='comment'),
    # path('<int:pk>/',views.blog_detail,name='detail'),
    # path('<int:pk>/comments/', views.comments_create, name='comments_create'),
    # path('<int:article_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),

    # path('write/',views.post,name='write'),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)