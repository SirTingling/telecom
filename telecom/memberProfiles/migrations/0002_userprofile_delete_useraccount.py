# Necessary imports:
# - `settings`: Contains the project's settings, useful for fetching global configurations like the AUTH_USER_MODEL.
# - `migrations`: Provides functionalities for creating and managing migrations.
# - `models`: Contains predefined field types and utilities for defining database models.
# - `deletion`: Contains behaviors to be applied when referenced objects in ForeignKey or OneToOneField are deleted.
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


# Defines a new migration class which provides instructions to the database for creating and modifying the database schema.
class Migration(migrations.Migration):

    # List of migrations that must be applied before applying this migration.
    dependencies = [
        # The default user model provided by Django (usually named "User").
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),

        # A previous migration in the 'memberProfiles' app.
        ('memberProfiles', '0001_initial'),
    ]

    # List of operations to be performed during this migration.
    operations = [
        # Create a new database table corresponding to the model `UserProfile`.
        migrations.CreateModel(
            name='UserProfile',  # The name of the new model/table.
            fields=[
                # An automatically incremented primary key for the model.
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                
                # An optional field to store a profile image. If not provided, a default image will be used.
                ('image', models.ImageField(
                    blank=True,
                    default='media/profileImage/male-user.png',
                    null=True,
                    upload_to='profileImage/',
                    verbose_name='Profile Image'
                )),
                
                # An optional unique field to store the user's phone number.
                ('phone_number', models.CharField(
                    blank=True,
                    max_length=20,
                    null=True,
                    unique=True,
                    verbose_name='Phone Number'
                )),
                
                # An optional field to store the user's date of birth.
                ('dob', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                
                # A field linking each profile to a unique user in the User model.
                # When the user is deleted, the associated profile will also be deleted (due to CASCADE).
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='profile',
                    to=settings.AUTH_USER_MODEL,
                    verbose_name='User'
                )),
            ],
        ),
        
        # Delete an existing model/table named `UserAccount`.
        migrations.DeleteModel(
            name='UserAccount',
        ),
    ]
