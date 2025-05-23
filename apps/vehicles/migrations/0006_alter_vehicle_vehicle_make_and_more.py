# Generated by Django 4.2.7 on 2024-04-03 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0005_alter_vehicle_availability_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_make',
            field=models.CharField(blank=True, choices=[('', 'Select Make'), ('Toyota', 'Toyota'), ('Honda', 'Honda'), ('Ford', 'Ford'), ('Chevrolet', 'Chevrolet'), ('Bmw', 'Bmw'), ('Mercedes Benz', 'Mercedes Benz'), ('Audi', 'Audi'), ('Nissan', 'Nissan'), ('Volkswagen', 'Volkswagen'), ('Tesla', 'Tesla')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='vehicle_type',
            field=models.CharField(blank=True, choices=[('', 'Select Type'), ('Sedan', 'Sedan'), ('Suv', 'Suv'), ('Truck', 'Truck'), ('Hatchback', 'Hatchback'), ('Coupe', 'Coupe'), ('Convertible', 'Convertible'), ('Mini Van', 'Mini Van'), ('Pickup', 'Pickup'), ('Van', 'Van'), ('Crossover', 'Crossover')], max_length=100, null=True),
        ),
    ]
