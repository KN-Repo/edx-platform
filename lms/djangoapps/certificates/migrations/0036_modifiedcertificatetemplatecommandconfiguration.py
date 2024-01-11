# Generated by Django 3.2.23 on 2024-01-11 22:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('certificates', '0035_auto_20230808_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModifiedCertificateTemplateCommandConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_date', models.DateTimeField(auto_now_add=True, verbose_name='Change date')),
                ('enabled', models.BooleanField(default=False, verbose_name='Enabled')),
                ('arguments', models.TextField(blank=True, default='', help_text="Arguments for the 'modify_cert_template' management command. Specify like '-template_ids <id1> <id2>'")),
                ('changed_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Changed by')),
            ],
            options={
                'verbose_name': 'modify_cert_template argument',
            },
        ),
    ]
