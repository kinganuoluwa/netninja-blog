from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from articles.views import article_list


urlpatterns = [
    path("admin/", admin.site.urls),
    path('', article_list, name='article_list'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
