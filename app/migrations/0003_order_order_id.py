# Generated by Django 2.2.5 on 2019-10-29 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_order_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='order_id',
            field=models.CharField(blank=True, max_length=120, null=True, unique=True),
        ),
    ]
