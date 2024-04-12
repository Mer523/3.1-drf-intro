from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_alter_measurement_created_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='sensor_id',
            new_name='sensor',
        ),
    ]
