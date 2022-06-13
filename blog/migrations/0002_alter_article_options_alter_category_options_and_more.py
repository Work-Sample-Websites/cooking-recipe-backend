# Generated by Django 4.0.4 on 2022-06-13 20:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Article', 'verbose_name_plural': 'Article'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Article Category', 'verbose_name_plural': 'Article Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='is_active',
        ),
    ]
