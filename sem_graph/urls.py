from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.emptyGraph, name='emptyGraph'),
    url(r'^(?P<graph_id>[0-9]+)/$', views.openGraph, name='openGraph'),
    url(r'^getNodes/?$', views.getNodes, name='getNodes'),
    url(r'^getEdges/?$', views.getEdges, name='getEdges'),
    url(r'^getGraph/?$', views.getGraphs, name='getGraph'),
    url(r'^pickGraph/(?P<graph_id>[0-9]+)/$', views.pickGraph, name='pickGraph'),
    url(r'^addNode/(?P<graph_id>[0-9]+)/$', views.addNode, name='addNode'),
    url(r'^addEdge/(?P<graph_id>[0-9]+)/$', views.addEdge, name='addEdge'),
    url(r'^editNode/$', views.editNode, name='editNode'),
]