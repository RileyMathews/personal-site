from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.
class HomePage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]

    parent_page_types = ['wagtailcore.Page']
    subpage_types = []

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)

        context['navigation_pages'] = self.get_children().live().in_menu()
        return context
