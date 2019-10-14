# Generated by Django 2.2.5 on 2019-10-14 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Issue', max_length=120)),
                ('body', models.TextField(help_text="What's wrong?")),
                ('upvotes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.Profile')),
            ],
            options={
                'db_table': 'issues',
            },
        ),
        migrations.CreateModel(
            name='Solution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Issue', max_length=120)),
                ('body', models.TextField()),
                ('upvotes', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Issue')),
            ],
            options={
                'db_table': 'solutions',
            },
        ),
    ]
