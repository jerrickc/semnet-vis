from django.contrib import admin
from .models import Node, Edge, EdgeType,Graph
# Register your models here.
admin.site.register(Graph)
admin.site.register(Node)
admin.site.register(Edge)
admin.site.register(EdgeType)