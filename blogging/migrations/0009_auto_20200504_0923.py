# Generated by Django 3.0.4 on 2020-05-04 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0008_auto_20200504_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='text1_bs',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text2_bs',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='text3_bs',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
