# Generated by Django 5.1.7 on 2025-03-31 15:45

import django.db.models.deletion
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        ('wagtailcore', '0094_alter_page_locale'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=wagtail.fields.StreamField([('paragraph', 0), ('image', 1)], block_lookup={0: ('wagtail.blocks.RichTextBlock', (), {'blank': True}), 1: ('wagtail.images.blocks.ImageBlock', [], {})}),
        ),
    ]
