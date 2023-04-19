# Generated by Django 4.1.7 on 2023-03-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_alter_patient_prescription_alter_patient_symptoms'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('room_number', models.IntegerField()),
                ('entry_time', models.DateTimeField(auto_now_add=True)),
                ('exit_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Doctor_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('slot_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transanction_id', models.IntegerField()),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('report_text', models.CharField(default=None, max_length=50)),
                ('report_image', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Test_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('test_type', models.CharField(default=None, max_length=50)),
                ('slot_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.IntegerField()),
                ('doctor_id', models.IntegerField()),
                ('prescription', models.CharField(default=None, max_length=50)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]