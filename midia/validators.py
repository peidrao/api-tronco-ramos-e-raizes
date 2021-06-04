from django.core.exceptions import ValidationError
import time

import datetime
import os
import unicodedata


from django.utils.deconstruct import deconstructible
from django.utils.encoding import force_text, force_str


# 2.5MB - 2621440
# 5MB - 5242880
# 10MB - 10485760
# 20MB - 20971520
# 50MB - 5242880
# 100MB - 104857600
# 250MB - 214958080
# 500MB - 429916160

def validate_file_size(self):
    file_size = self.size

    if file_size > 20971520:
        raise ValidationError('Tamanho máximo de arquivo é de 20MB')
    else:
        return self

@deconstructible
class UploadToPath(object):
    def __init__(self, upload_to):
        self.upload_to = upload_to

    def __call__(self, instance, filename):
        return self.generate_filename(filename)

    def get_directory_name(self):
        return os.path.normpath(force_text(datetime.datetime.now().strftime(force_str(self.upload_to))))

    def get_filename(self, filename):
        now = time.time()
        extension = filename.split('.')[-1]
        stamp = datetime.datetime.fromtimestamp(now).strftime('%Y-%m-%d-%H-%M-%S')
        return '{0}_.{1}'.format(str(stamp), extension)


    def generate_filename(self, filename):
        return os.path.join(self.get_directory_name(), self.get_filename(filename))