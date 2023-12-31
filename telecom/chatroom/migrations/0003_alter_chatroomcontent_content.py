

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0002_alter_chatroomcontent_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroomcontent',
            name='content',
            field=models.CharField(default=django.utils.timezone.now, max_length=10000),
            preserve_default=False,
        ),
    ]
