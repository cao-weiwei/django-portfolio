# Generated by Django 2.2.17 on 2021-02-02 16:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=254)),
                ('url', models.URLField(blank=True)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('blog_post', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.BlogPost')),
            ],
            options={
                'verbose_name': '评论',
                'verbose_name_plural': '评论列表',
            },
        ),
    ]
