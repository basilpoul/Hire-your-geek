# Generated by Django 4.1.4 on 2023-03-03 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GEEK', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Warning',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msg', models.CharField(max_length=20)),
                ('cid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GEEK.coders')),
            ],
        ),
    ]
