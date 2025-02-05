# Generated by Django 2.2.1 on 2019-05-21 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('role', '0004_auto_20190521_0001'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInterests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_interests', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
                ('tipos_role', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_interests', to='role.TiposRole', verbose_name='Genero')),
            ],
        ),
    ]
