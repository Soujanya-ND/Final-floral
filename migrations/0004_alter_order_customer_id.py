# Generated by Django 3.2.7 on 2022-03-22 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('floral', '0003_alter_order_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.IntegerField(null=True),
        ),
    ]