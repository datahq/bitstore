import os
from filemanager.models import FileManager

db_connection_string = os.environ.get('DATABASE_URL')
FileRegistry = FileManager(db_connection_string)
