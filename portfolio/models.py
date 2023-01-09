from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase

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


class ProjectPageTag(TaggedItemBase):
    content_object = ParentalKey('portfolio.ProjectPage', on_delete=models.CASCADE, related_name='tagged_items')


class ProjectPage(Page):
    description = RichTextField()
    short_description = models.TextField(max_length=255, default='')
    repository_url = models.URLField(blank=True)
    tags = ClusterTaggableManager(through=ProjectPageTag, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('repository_url'),
        FieldPanel('tags'),
    ]

    parent_page_types = ['portfolio.PortfolioIndexPage']
    subpage_types = []
