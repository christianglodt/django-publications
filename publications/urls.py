__license__ = 'MIT License <http://www.opensource.org/licenses/mit-license.php>'
__author__ = 'Lucas Theis <lucas@theis.io>'
__docformat__ = 'epytext'

from django.conf.urls import url

import publications.views

urlpatterns = [
	url(r'^$', publications.views.year),
	url(r'^(?P<publication_id>\d+)/$', publications.views.id),
	url(r'^year/(?P<year>\d+)/$', publications.views.year),
	url(r'^tag/(?P<keyword>.+)/$', publications.views.keyword),
	url(r'^list/(?P<list>.+)/$', publications.views.list),
	url(r'^(?P<name>.+)/$', publications.views.person),
]
