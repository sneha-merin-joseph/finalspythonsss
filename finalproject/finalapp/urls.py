


from django.urls import path
from . import views
urlpatterns = [
    path('', views.demo, name='demo'),
    path('home', views.home, name='home'),
    path('ho', views.ho, name='ho'),
    path('hom', views.hom, name='hom'),
    path('homes', views.homes, name='homes'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('details', views.details, name='details'),
    path('det', views.det, name='det'),
    path('deta', views.deta, name='deta'),
    path('add/', views.add_movie, name='add_movie'),
    path('review', views.review, name='review'),
    # path('add',views.add_movi,name='add_movi'),
    path('detail/<int:movie_id>/', views.detail, name='detail'),
    path('de/<int:movie_id>/', views.de, name='de'),
    path('update/<int:id>/', views.update, name='update'),
    # path('update/<int:id>/',views.update,name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('cut/<int:id>/', views.cut, name='cut'),
    path('index', views.index, name='index'),
    path('film', views.film, name='film'),
    path('rev', views.rev, name='rev'),
    path('reviews', views.reviews, name='reviews'),
    path('reviewSs', views.reviewSs, name='reviewSs'),
    path('romance', views.romance, name='romance'),
    path('cri', views.cri, name='cri'),
    path('comedy', views.comedy, name='comedy'),
    path('horror', views.horror, name='horror'),
    path('emot', views.emot, name='emot'),
    path('search',views.search,name='search'),
    # path('', views.SearchResult, name='SearchResult'),

]