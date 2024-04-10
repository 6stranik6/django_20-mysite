# Generated by Django 4.2.7 on 2024-01-18 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0009_alter_order_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='descriptions',
            field=models.TextField(blank=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=100),
        ),
    ]