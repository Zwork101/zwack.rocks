from blog.models import BlogPost, BlogIndexPage

from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    description = RichTextField(blank=True)
    
    content_panels = Page.content_panels + ["description"]
    
    def get_context(self, request):
        context = super().get_context(request)
        context['current_post'] = BlogPost.objects.order_by("-first_published_at").first()
        context['blog'] = BlogIndexPage.objects.first()
        return context
    
    
