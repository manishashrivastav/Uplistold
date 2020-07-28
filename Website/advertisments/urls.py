from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
app_name = 'advertisements'
urlpatterns = [
               path('' , views.index , name = 'index'),
               path('index/' , views.index , name = 'index'),
               path('login/' , auth_views.LoginView.as_view(template_name ='login.html') , name = 'login'),
               path('register/' , views.register , name = 'register'),
               path('logout/', auth_views.LogoutView.as_view(template_name ='logout.html'), name='logout'),
               path('password_reset/', auth_views.PasswordResetView.as_view(template_name ='password_reset.html'),
                    name='password_reset'),
               path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(
                   template_name ='password_reset_done.html'), name='password_reset_done'),
               path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
                   template_name ='password_reset_confirm.html'), name='password_reset_confirm'),
               path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
                   template_name ='password_reset_complete.html'), name='password_reset_complete'),
               path('ad-listing/' , views.ad_listing , name = 'ad_listing'),
               path('terms_condition/' , views.terms_condition , name = 'terms_condition'),
               path('contact_us/' , views.contact_us , name = 'contact_us'),
               path('about_us/' , views.about_us , name = 'about_us'),
               path('reply_contact', views.reply_contact , name = 'reply_contact'),
               path('user_profile/' , views.user_profile , name = 'user_profile'),
               path('user_profile2/', views.user_profile2, name='user_profile2'),
               path('update_profile_pic/<int:id>' , views.update_profile_pic , name = 'update_profile_pic'),
               path('change_password' , views.change_password , name ='change_password'),
               path('location_update/' , views.location_update , name ='location_update'),
               path('location_update_again/<int:id>', views.location_update_again, name='location_update_again'),
               path('my_ads/' , views.my_ads , name ='my_ads'),
               path('pending_ads/' , views.pending_ads , name ='pending_ads'),
               path('category/' , views.category , name ='category'),
               path('<int:pk>/' , views.details , name ='details'),
               path('update/<int:id>/' , views.update , name ='update'),
               path('delete/<int:id>/' , views.delete , name ='delete'),
               path('ad_details/<int:pk>/' , views.ad_details , name ='ad_details'),
               path('review/<int:id>' , views.review , name ='review'),
               path('ad_list_view/<int:id>' , views.ad_list_view , name='ad_list_view'),
               path('store/<int:id>/' , views.store , name='store'),
               path('search/' , views.search , name='search'),
               path('ad_list/' , views.ad_list , name='ad_list'),
               path('outbox/' , views.outbox , name='outbox'),
               path('delete_user/' , views.delete_user , name='delete_user'),
]


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

