# Generated by Django 3.0.7 on 2020-07-12 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('advertisments', '0004_auto_20200708_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='advertisments.Review'),
        ),
    ]
