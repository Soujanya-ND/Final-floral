# Generated by Django 3.2.7 on 2022-03-23 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('floral', '0005_alter_order_customer_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='looksafter',
        ),
        migrations.AlterField(
            model_name='order',
            name='customer_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='floral.customer'),
        ),
    ]
