from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
import home.urls
from django.conf.urls.i18n import i18n_patterns
import identity.urls

urlpatterns = i18n_patterns(
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(home.urls, namespace='home')),
)

urlpatterns += [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^identity/', include(identity.urls, namespace='identity')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
