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
    subpage_types = ['portfolio.ProjectPage']

    def get_context(self, request, *args, **kwargs):
        context = super(PortfolioIndexPage, self).get_context(request, *args, **kwargs)

        context['project_pages'] = self.get_children().live().specific()
        return context


class ProjectPage(Page):
    description = RichTextField()
    repository_url = models.URLField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('repository_url'),
    ]

    parent_page_types = ['portfolio.PortfolioIndexPage']
    subpage_types = []
