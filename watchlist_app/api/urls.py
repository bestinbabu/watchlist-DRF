from watchlist_app.api.views import ReviewDetail, ReviewCreate,ReviewList, UserReview, WatchListAV,WatchListDetailAV,StreamPlatformAV,StreamPlatformDetailAV
from django.urls import path
 

urlpatterns = [
    path('list/', WatchListAV.as_view(),name='watchlist-list')  ,
    path('<int:pk>/',WatchListDetailAV.as_view(),name='watchlist-detail'),
    
    path('stream/',StreamPlatformAV.as_view(),name='streamplatform-list'),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name='streamplatform-detail'),
    
    path('<int:pk>/reviews/',ReviewList.as_view(),name='reviewlist-detail'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
    
    path('reviews/',UserReview.as_view(),name='user-reviews')
    
    # path('review/',ReviewList.as_view(),name='reviewlist-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(),name='reviewlist-list'),
    
]