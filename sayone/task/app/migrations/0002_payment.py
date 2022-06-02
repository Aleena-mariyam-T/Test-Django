# Generated by Django 4.0.4 on 2022-06-01 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ticket', models.CharField(choices=[('Gold', 'Gold'), ('Platinum', 'Platinum'), ('Silver', 'Silver')], default='Silver', max_length=30)),
                ('price', models.FloatField()),
            ],
        ),
    ]
