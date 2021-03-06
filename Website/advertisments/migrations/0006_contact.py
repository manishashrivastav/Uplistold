# Generated by Django 3.0.7 on 2020-07-14 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('advertisments', '0005_review_review_parent'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='None', max_length=30)),
                ('subject', models.CharField(default='None', max_length=40)),
                ('message', models.CharField(default='None', max_length=200)),
                ('reply', models.CharField(default='No Reply', max_length=200)),
                ('post_date_contact', models.DateField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
