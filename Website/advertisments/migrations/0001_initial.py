# Generated by Django 3.0.7 on 2020-07-04 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ad_title', models.CharField(default='None', max_length=200)),
                ('condition', models.CharField(default='Not Mentioned', max_length=200)),
                ('ad_brand', models.CharField(default='Not Mentioned', max_length=200)),
                ('ad_model', models.CharField(default='Not Mentioned', max_length=200)),
                ('ad_price', models.FloatField(default='Not on Sale')),
                ('ad_description', models.CharField(default='Not Mentioned', max_length=200)),
                ('ad_image1', models.ImageField(default='No Images', upload_to='images/')),
                ('ad_image2', models.ImageField(default='No Images', upload_to='images/')),
                ('ad_image3', models.ImageField(default='No Images', upload_to='images/')),
                ('ad_status', models.BooleanField(default=True)),
                ('post_date', models.DateField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(default='Other Category', max_length=200)),
                ('cat_image', models.ImageField(blank=True, default='No Image', upload_to='cat_images/')),
                ('cat_status', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('sub_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(default='Others', max_length=200)),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='advertisments.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, default='None', max_length=100)),
                ('ad_review', models.CharField(default='None', max_length=500)),
                ('post_date_review', models.DateField(auto_now_add=True, null=True)),
                ('name_of_customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('review_of_ad', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='advertisments.Ad')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.CharField(default='', max_length=10)),
                ('ad_profile_pic', models.ImageField(blank=True, default='', upload_to='profile_images/')),
                ('user_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(default='Not Mentioned', max_length=200)),
                ('city', models.CharField(default='Not Mentioned', max_length=200)),
                ('state', models.CharField(default='Not Mentioned', max_length=200)),
                ('pin_code', models.CharField(default='000000', max_length=6)),
                ('user_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ad',
            name='ad_cat',
            field=models.ForeignKey(default=0, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_cat', to='advertisments.Category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='ad_subcat',
            field=models.ForeignKey(default=0, max_length=20, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ad_subcat', to='advertisments.sub_category'),
        ),
        migrations.AddField(
            model_name='ad',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
