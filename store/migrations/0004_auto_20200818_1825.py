# Generated by Django 3.0.8 on 2020-08-18 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=0, upload_to='product'),
            preserve_default=False,
        ),
    ]