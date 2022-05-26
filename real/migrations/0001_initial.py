# Generated by Django 4.0.4 on 2022-05-26 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('dep_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('dept_head', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('discipline_score', models.CharField(default='', max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('image', models.ImageField(default='', upload_to='teachers/')),
                ('dep_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='real.department')),
            ],
        ),
    ]
