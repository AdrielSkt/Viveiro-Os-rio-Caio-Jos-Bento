# Generated by Django 4.0.5 on 2022-06-15 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Flores', '0002_alter_flores_id_alter_flores_link_alter_flores_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flores',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
