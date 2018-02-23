from django.urls import path
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import CreateTrackDataView, indexView, DetailsView

app_name = 'api'

urlpatterns = {
    path('', indexView, name='index'),
    url(r'^trackdata/$', CreateTrackDataView.as_view(), name='trackdata'),
    url(r'^trackdata/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details")
}


urlpatterns = format_suffix_patterns(urlpatterns)
