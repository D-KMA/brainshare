# Generated by Django 3.0.3 on 2020-05-31 22:29

import blogapp.files
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('slug', models.SlugField(help_text='This field is prepopulated with the username of the profile', verbose_name='Slug')),
                ('banner', models.ImageField(blank=True, help_text='An image used as your banner', max_length=255, null=True, upload_to=blogapp.files.AuthorBanner, verbose_name='Banner')),
                ('image', models.ImageField(blank=True, help_text='An image used as your Display picture', null=True, upload_to=blogapp.files.AuthorImage, verbose_name='Profile picture')),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(blank=True, choices=[('BrainShare', 'BrainShare'), ('Facebook', 'Facebook'), ('Twitter', 'Twitter'), ('Instagram', 'Instagram'), ('Tumblr', 'Tumblr'), ('LinkedIn', 'LinkedIn'), ('Pinterest', 'Pinterest'), ('Telegram', 'Telegram'), ('YouTube', 'YouTube'), ('Discord', 'Discord'), ('Github', 'Github'), ('Slack', 'Slack')], help_text='Select a social media platform', max_length=100, null=True, verbose_name='Platform')),
                ('handle', models.CharField(blank=True, help_text='What is your username on this platform', max_length=200, null=True, verbose_name='Handle')),
                ('link', models.URLField(blank=True, help_text='Full address (link) to your page', null=True, verbose_name='Link to your page')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Author')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, help_text='The title of this post', max_length=255, null=True, verbose_name='Title')),
                ('slug', models.SlugField(blank=True, help_text='This field is prepopulated with the title field', max_length=255, null=True, verbose_name='Slug')),
                ('concern', models.CharField(default='', help_text='<p>What does this post talk about</p><p>E.G programming, politics..</p>', max_length=200, verbose_name='Concern')),
                ('banner', models.ImageField(blank=True, help_text='An image displayed along side the title', max_length=255, null=True, upload_to=blogapp.files.PostBanner, verbose_name='Banner')),
                ('banner_copyright', models.CharField(blank=True, default='', help_text='Where this image was gotten from', max_length=255, null=True, verbose_name='Copyright')),
                ('banner_copyright_link', models.URLField(blank=True, default='', help_text='Link to where this image was taken from', max_length=255, null=True, verbose_name='Copyright link')),
                ('tags', models.TextField(blank=True, help_text='Terms concerning this post. E.G. programming, politics', null=True, verbose_name='Tags')),
                ('heading', models.CharField(blank=True, help_text='The main heading of this post', max_length=255, null=True, verbose_name='Heading')),
                ('text_content', models.TextField(blank=True, help_text='Text content of this post', null=True, verbose_name='Text Content')),
                ('image', models.ImageField(blank=True, help_text='<p>If the post requires an image, upload one here</p><p>More images can be uploaded from the more section</p>', max_length=255, null=True, upload_to=blogapp.files.PostImage, verbose_name='Image')),
                ('image_copyright', models.CharField(blank=True, default='', help_text='Where this image was gotten from', max_length=255, null=True, verbose_name='Copyright')),
                ('image_copyright_link', models.URLField(blank=True, default='', help_text='Link to where this image was taken from', max_length=255, null=True, verbose_name='Copyright link')),
                ('list_style', models.CharField(choices=[('Ordered List (numeric)', 'Ordered List (numeric)'), ('Unordered List (bullet)', 'Unordered List (bullet)')], default='Ordered List (numeric)', help_text='How the list should be displayed', max_length=100, verbose_name='List Style')),
                ('list_content', models.TextField(blank=True, help_text='This fields converts comma seperated texts into list', null=True, verbose_name='List Content')),
                ('code', models.TextField(blank=True, help_text='Add code samples to post for better understanding', null=True, verbose_name='Code')),
                ('date_to_publish', models.DateTimeField(default=django.utils.timezone.now, help_text='When should this post be published? Default is now.', verbose_name='Publish Date')),
                ('status', models.CharField(blank=True, help_text='The status of the post, if published or drafted', max_length=255, null=True, verbose_name='Status')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Author')),
            ],
        ),
        migrations.CreateModel(
            name='MoreContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(blank=True, help_text='Heading of this content if any', max_length=255, null=True, verbose_name='Heading')),
                ('text_content', models.TextField(blank=True, help_text='Text content if any', null=True, verbose_name='Text Content')),
                ('image', models.ImageField(blank=True, help_text='Add more images to the post', max_length=255, null=True, upload_to=blogapp.files.MorePostImage, verbose_name='Image')),
                ('image_copyright', models.CharField(blank=True, default='', help_text='Where this image was gotten from', max_length=255, null=True, verbose_name='Copyright')),
                ('image_copyright_link', models.URLField(blank=True, default='', help_text='Link to where this image was taken from', max_length=255, null=True, verbose_name='Copyright link')),
                ('list_style', models.CharField(choices=[('Ordered List (numeric)', 'Ordered List (numeric)'), ('Unordered List (bullet)', 'Unordered List (bullet)')], default='Ordered List (numeric)', help_text='How the list should be displayed', max_length=100, verbose_name='List Style')),
                ('list_content', models.TextField(blank=True, help_text='This fields converts comma seperated texts into list', null=True, verbose_name='List Content')),
                ('code', models.TextField(blank=True, help_text='Add more code samples', null=True, verbose_name='Code')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blogapp.Post')),
            ],
        ),
    ]
