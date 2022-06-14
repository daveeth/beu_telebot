# Generated by Django 3.2.3 on 2022-06-14 13:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_num', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='TelegramChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=128, unique=True)),
                ('type', models.CharField(choices=[('private', 'private'), ('group', 'group'), ('supergroup', 'supergroup'), ('channel', 'channel')], max_length=128)),
                ('title', models.CharField(blank=True, max_length=512, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telegram_id', models.CharField(max_length=128, unique=True)),
                ('is_bot', models.BooleanField(default=False)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(blank=True, max_length=128, null=True)),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('phone_num', models.TextField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.TextField()),
                ('quantity', models.IntegerField(default=0)),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('order_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='our_beu_delivery_bot.telegramuser')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='our_beu_delivery_bot.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=6)),
                ('rest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='our_beu_delivery_bot.restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='TelegramState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memory', models.TextField(blank=True, null=True, verbose_name='Memory in JSON format')),
                ('name', models.CharField(blank=True, max_length=256, null=True)),
                ('telegram_chat', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_states', to='our_beu_delivery_bot.telegramchat')),
                ('telegram_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_states', to='our_beu_delivery_bot.telegramuser')),
            ],
            options={
                'unique_together': {('telegram_user', 'telegram_chat')},
            },
        ),
    ]
