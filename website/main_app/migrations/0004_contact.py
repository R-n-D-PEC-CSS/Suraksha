# Generated by Django 3.0.6 on 2020-05-20 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main_app', '0003_auto_20200520_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('relation', models.CharField(choices=[('Father', 'Father'), ('Mother', 'Mother'), ('Brother', 'Brother'), ('Sister', 'Sister'), ('Husband', 'Husband'), ('Friend', 'Friend'), ('Relative', 'Relative'), ('Other', 'Other')], max_length=20)),
            ],
        ),
    ]
