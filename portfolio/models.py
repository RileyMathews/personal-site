from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel

# Create your models here.
class PortfolioIndexPage(Page):
    body = RichTextField()

    content_panels = Page.content_panels + [
        FieldPanel("body")
    ]

    parent_page_types = ['home.HomePage']
    subpage_types = []
