# Generated by Django 3.0.4 on 2020-05-04 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0010_auto_20200504_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='header1_bs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='header2_bs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='name_person_bs',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo_bs',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='photo_person_bs',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text1_bs',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text2_bs',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text_person_bs',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
    ]
