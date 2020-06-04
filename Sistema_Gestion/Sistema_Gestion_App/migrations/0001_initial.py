# Generated by Django 3.0.6 on 2020-06-02 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('seccion', models.CharField(default='', max_length=20)),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('marca', models.CharField(default='', max_length=20)),
                ('unidad', models.CharField(default='', max_length=20)),
                ('codigo', models.CharField(default='', max_length=20)),
                ('lote', models.CharField(default='', max_length=20)),
            ],
        ),
    ]