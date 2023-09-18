

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chatroom', '0003_alter_chatroomcontent_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroomcontent',
            name='chatroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatroom.chatroom'),
        ),
    ]
