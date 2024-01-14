# Generated by Django 5.0.1 on 2024-01-14 11:21

import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import main.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], message="Quyidagi formatdagi rasmni kiriting('png','jpeg','jpg')")])),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last_name')),
                ('info', models.TextField(blank=True)),
            ],
            bases=(models.Model, main.models.ImageClass),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], message="Quyidagi formatdagi rasmni kiriting('png','jpeg','jpg')")])),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first_name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last_name')),
                ('phone', models.CharField(blank=True, max_length=13, validators=[django.core.validators.MinLengthValidator(9, message="Nomerni to'liq kiriting"), django.core.validators.MaxLengthValidator(13, message="Nomerni to'g'ri kiriting")])),
            ],
            bases=(models.Model, main.models.ImageClass),
        ),
        migrations.CreateModel(
            name='Employee',
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
                ('phone', models.CharField(blank=True, max_length=13, validators=[django.core.validators.MinLengthValidator(9, message="Nomerni to'liq kiriting"), django.core.validators.MaxLengthValidator(13, message="Nomerni to'g'ri kiriting")])),
                ('image', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], message="Quyidagi formatdagi rasmni kiriting('png','jpeg','jpg')")])),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Xodim',
                'verbose_name_plural': 'Xodimlar',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpeg', 'jpg'], message="Quyidagi formatdagi rasmni kiriting('png','jpeg','jpg')")])),
                ('name', models.CharField(blank=True, max_length=150, verbose_name='name')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main.author')),
            ],
        ),
        migrations.CreateModel(
            name='AcceptedBooks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.book')),
            ],
        ),
        migrations.CreateModel(
            name='BookRecevier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('books', models.ManyToManyField(to='main.acceptedbooks')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
