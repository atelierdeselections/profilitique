from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from programmes.views import ChoisirWizard

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'moi_candidat.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'programmes.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),

	url(r'^programmes/$', 'programmes.views.programmes'),

    url(r'^choisir/$', ChoisirWizard.as_view()),
	url(r'^resultat/(?P<hashcode>\w+)/$', 'programmes.views.resultat'),
	url(r'^mon-programme/(?P<hashcode>\w+)/$', 'programmes.views.mon_programme'),

	url(r'^export/$', 'programmes.views.export_csv'),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
