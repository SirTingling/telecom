# Django's auto-generated migration file.

# Necessary imports:
# - `settings`: Contains the project's settings, useful for fetching global configurations like the AUTH_USER_MODEL.
# - `migrations`: Provides functionalities for creating and managing migrations.
# - `models`: Contains predefined field types and utilities for defining database models.
# - `deletion`: Contains behaviors to be applied when referenced objects in ForeignKey or OneToOneField are deleted.
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

# Define a migration class, containing instructions for database schema changes.
class Migration(migrations.Migration):

    # Indicates that this is the initial migration for the app.
    initial = True

    # Specifies which migrations should be applied before this one.
    # In this case, it depends on the default user model provided by Django.
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    # List of operations to be performed during this migration.
    operations = [
        # Create a new database model named `UserAccount`.
        migrations.CreateModel(
            name='UserAccount',  # Name of the new model/table.
            fields=[
                # Auto-incremented primary key for the model.
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                # Optional profile image for the user. 
                # Uses a default image if none is provided.
                ('image', models.ImageField(blank=True, default='appMedia/person.png', null=True, upload_to='profileImage')),
                
                # Optional unique phone number field.
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                
                # Optional date of birth field.
                ('dob', models.DateField(blank=True, null=True)),
                
                # One-to-one relation with the user model.
                # This means each user can have only one profile.
                # If the user is deleted, the associated UserAccount entry will also be deleted (due to CASCADE behavior).
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
