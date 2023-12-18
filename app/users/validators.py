from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


# Custom validator for document field, it may be:
#       8 digits + letter,
#       1 letter + 8 digits,
#       3letters + 6 digits or
#       alphabetical + date
class DocumentValidator(BaseValidator):
    message = 'Document is not valid'
    code = 'invalid'

    def __init__(self, document=None):
        super().__init__(document)

    def __call__(self, document):
        if document is not None:
            document = document.upper()
            if len(document) != 9:
                # Alphanumeric with date
                date = document[-8:]
                alpha = document[:-8]
                if not alpha.isalpha() or not date.isnumeric():
                    raise ValidationError(self.message, code=self.code)
            else:
                # 8 digits + letter or 1 letter + 8 digits or 3letters + 6 digits
                # I'm sorry for these if statements, but if you have a better idea go on!
                if not document[:-1].isnumeric() or not document[-1].isalpha():
                    if not document[0].isalpha() or not document[1:].isnumeric():
                        if not document[:3].isalpha() or not document[3:].isnumeric():
                            raise ValidationError(self.message, code=self.code)
        else:
            raise ValidationError(self.message, code=self.code)


class PasswordValidator(BaseValidator):
    message = 'Password is not valid'
    code = 'invalid'

    def __init__(self, password=None):
        super().__init__(password)

    def __call__(self, password):
        if password is not None:
            if len(password) < 4:
                raise ValidationError(self.message, code=self.code)
        else:
            raise ValidationError(self.message, code=self.code)
