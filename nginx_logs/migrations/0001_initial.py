# Generated by Django 5.1.1 on 2024-09-24 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ParseLogs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.CharField(blank=True, max_length=100, null=True, verbose_name='IP-адрес')),
                ('date_log', models.DateTimeField(blank=True, null=True, verbose_name='Дата лога')),
                ('method', models.CharField(blank=True, max_length=100, null=True, verbose_name='HTTP метод')),
                ('url', models.CharField(blank=True, max_length=200, null=True, verbose_name='URL')),
                ('status_code', models.IntegerField(blank=True, null=True, verbose_name='HTTP статус код')),
                ('size', models.IntegerField(blank=True, null=True, verbose_name='Размер ответа')),
            ],
            options={
                'verbose_name': 'Лог парсинга',
                'verbose_name_plural': 'Логи парсинга',
            },
        ),
    ]
