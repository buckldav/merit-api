# Icons

## Generate Font Awesome Name Tuples

This is for use in Django apps that store Font Awesome icon names in the models. `names.py` is a list of tuples to be used as the `choices` kwarg in a `CharField` or `IntegerField`

### Run TypeScript file

Source: `generateFaNames.ts`

```bash
npm install
npm run faNames
# Output File = names.py
```

### Use Choices in Django Model

```python
from django.db import models
from icons.names import FA_ICON_NAMES

class MyModel(models.Model):
    # The maximum icon name length is 34, so put 50 in the model to be safe.
    fa_icon_name = models.CharField(max_length=50, choices=FA_ICON_NAMES)
```
