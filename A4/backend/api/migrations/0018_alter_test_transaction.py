# Generated by Django 4.1.7 on 2023-03-03 08:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_delete_test_appointment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='transaction',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.transaction'),
        ),
    ]