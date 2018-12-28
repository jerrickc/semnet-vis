from django import template
import json

register = template.Library()

@register.simple_tag
def jsonify(string):
    return json.dumps(string)