from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager


class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
    ]

class TechnologyTag(TaggedItemBase):
    content_object = ParentalKey(
        'ProjectPage',
        related_name='tagged_items',
        on_delete=models.CASCADE,
    )

class ProjectPage(Page):
    description = RichTextField(blank=True)
    code_repository_url = models.URLField(blank=True)
    technologies = ClusterTaggableManager(through=TechnologyTag, blank=True)


    content_panels = Page.content_panels + [
        FieldPanel("description"),
        FieldPanel("code_repository_url"),
        MultiFieldPanel([
            FieldPanel('technologies')
        ])
    ]
