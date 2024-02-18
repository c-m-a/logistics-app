# Generated by Django 4.2.10 on 2024-02-18 18:21

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('logistics', '0002_courier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=128, primary_key=True, serialize=False, unique=True)),
                ('dimensions', models.CharField(max_length=32)),
                ('weight', models.CharField(max_length=32)),
                ('destination_address', models.CharField(max_length=32)),
                ('origin_address', models.CharField(max_length=32)),
                ('status', models.CharField(choices=[('created', 'Created'), ('assigned', 'Assigned'), ('delivered', 'Delivered')], default='created', max_length=20)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('assigned_courier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='assigned_packages', to='logistics.courier')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_packages', to='logistics.customer')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
