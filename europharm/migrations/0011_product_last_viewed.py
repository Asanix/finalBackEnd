# Generated by Django 4.2 on 2023-05-02 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('europharm', '0010_alter_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='last_viewed',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
