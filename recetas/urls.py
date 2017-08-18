from django.conf.urls import url, include
from recetas import views
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.authtoken import views as views_rest
from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static

from django.views.static import serve

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'recetas', views.RecetaViewSet)
router.register(r'ingredientes', views.IngredienteViewSet)
router.register(r'implementos', views.ImplementoViewSet)
router.register(r'versiones', views.VersionViewSet)


schema_view = get_schema_view(title='Pastebin API')

urlpatterns = [
    url(r'^schema/$', schema_view),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', views_rest.obtain_auth_token),
    url(r'^api-token-generate/', views.get_all_tokens),
    url(r'^admin/password_reset/$', auth_views.password_reset,
        name='admin_password_reset'),
    url(r'^admin/password_reset/done/$',
        auth_views.password_reset_done, name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.password_reset_complete,
        name='password_reset_complete'),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': settings.DEBUG}),

]
