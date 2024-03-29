# Generated by Django 5.0 on 2023-12-13 18:52

import django.contrib.auth.models
import django.contrib.auth.validators
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='HoroskopModel',
            fields=[
                ('zodiac', models.CharField(choices=[('ARIES', 'Aries'), ('TAURUS', 'Taurus'), ('GEMINI', 'Gemini'), ('CANCER', 'Cancer'), ('LEO', 'Leo'), ('VIRGO', 'Virgo'), ('LIBRA', 'Libra'), ('SCORPIO', 'Scorpio'), ('SAGITTARIUS', 'Sagittarius'), ('CAPRICORN', 'Capricorn'), ('AQUARIUS', 'Aquarius'), ('PISCES', 'Pisces')], primary_key=True, serialize=False)),
                ('description', models.CharField()),
                ('date_create_zodiac', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(choices=[('all', 'all'), ('Minsk', 'Minsk'), ('Moscow', 'Moscow')], default='all', max_length=20)),
                ('date', models.DateField()),
                ('temperature', models.IntegerField()),
                ('pressure', models.IntegerField()),
                ('wind', models.FloatField()),
                ('weather', models.CharField(choices=[('SUN', 'Sun'), ('RAIN', 'Rain'), ('FOGGY', 'Foggy')], default='SUN', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('user_zodiac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_weather.horoskopmodel')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='SiteUserModel',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=30)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('user_zodiac', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='site_weather.horoskopmodel')),
            ],
        ),
    ]
