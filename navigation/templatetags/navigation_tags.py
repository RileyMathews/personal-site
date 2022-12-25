from django import template
from wagtail.models import Site

register = template.Library()

@register.simple_tag(takes_context=True)
def get_root_page_menu(context):
    return Site.find_for_request(context['request']).root_page.get_children().live().in_menu()
