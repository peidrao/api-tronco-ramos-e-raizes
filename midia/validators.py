from django.core.exceptions import ValidationError

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