# Generated by Django 3.2.3 on 2022-06-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beu_admin_bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramchat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='telegramstate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
