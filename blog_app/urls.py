from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('post/<slug:post_slug>/', PostPageView.as_view(), name='post'),
    path('category/<slug:category_slug>/', CategoryListView.as_view(), name='category'),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('signup/', SignupFormView.as_view(), name='signup'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
]