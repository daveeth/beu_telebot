# Generated by Django 3.2.3 on 2022-06-15 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_beu_delivery_bot', '0003_alter_food_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=12),
        ),
    ]