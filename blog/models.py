from bs4 import BeautifulSoup
from django.db import models
from html import unescape

from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageBlock

class BlogIndexPage(Page):
    subpage_types = ["blog.BlogPost"]


class BlogPost(Page):
    subpage_types = ["blog.BlogIndexPage"]
    
    content = StreamField([
        ("paragraph", RichTextBlock(blank=True)),
        ("image", ImageBlock())
    ], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.TextField(blank=True)
    
    trailer = models.TextField(blank=True)
    
    content_panels = Page.content_panels + ["author", "content"]
    
    def primary_image(self):
        img = next((img for img in self.content if img.block_type == 'image'), None)
        return img.value.file.url if img else None
    
    def save(self, *args, **kwargs):
        txt = next((txt for txt in self.content if txt.block_type == "paragraph"), "")
        if txt != "":
            txt = BeautifulSoup(unescape(txt.value.source), "html.parser").text
            if len(txt) > 80:
                txt = txt[:77] + "..."
        self.trailer = txt
        return super().save(*args, **kwargs)
        