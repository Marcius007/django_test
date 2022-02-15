# Generated by Django 4.0.2 on 2022-02-13 10:54

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_profile_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('post_msg', models.TextField()),
                ('post_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.ManyToManyField(to='core.Profile')),
            ],
        ),
    ]
