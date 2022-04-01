# Generated by Django 3.0.7 on 2021-02-01 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210201_2139'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='click_counter',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='summary',
            field=models.TextField(default='', max_length=150),
        ),
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(),
        ),
    ]