from django.urls import path, include
from . import views, views_generics
from .views_model_viewset import ArticleModelViewset
from .views_generic_viewset import ArticleGenericViewset
from .views_viewset import ArticleViewset
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('article', ArticleViewset, basename='article')
router.register('article', ArticleGenericViewset, basename='article-viewset')
router.register('article', ArticleModelViewset, basename='article-model-viewset')

urlpatterns = [
    #& fuction based views
    path('article/', views.articles_list ),
    path('article/<str:pk>/', views.article_detail ),

    #& class based views
    path('class/article/', views.ArticleAPIView.as_view() ),
    path('class/article/<str:id>/', views.ArticleDetailsAPIView.as_view() ),

    #& generics based views
    path('generics/article/', views_generics.ArticleGenericView.as_view() ),

    #& generic and mixins based views
    path('generics/mixins/article/', views_generics.ArticleGenericMixinView.as_view() ),
    path('generics/mixins/article/<int:id>/', views_generics.ArticleGenericMixinView.as_view() ),

    #& viewset based views
    path('viewset/', include(router.urls) ),
    path('viewset/<int:pk>/', include(router.urls) ),

    #& generic viewset based views
    path('generics/mixins/viewset/', include(router.urls) ),
    path('generics/mixins/viewset/<int:pk>/', include(router.urls) ),

    #& generic viewset based views
    path('model/viewset/', include(router.urls) ),
    path('model/viewset/<int:pk>/', include(router.urls) ),
]
