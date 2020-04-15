# Generated by Django 3.0.4 on 2020-04-15 10:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_delete_booking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='photo',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='chefs',
            name='position',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Category'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='food_image',
            field=models.ImageField(null=True, upload_to='photos/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='is_on_home_page',
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='is_published',
            field=models.BooleanField(default=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='price',
            field=models.IntegerField(null=True),
        ),
    ]
