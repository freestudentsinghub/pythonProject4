from django.forms import ModelForm, forms

from catalog.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    banned_words = [
        'казино',
        'криптовалюта',
        'крипта',
        'биржа',
        'дешево',
        'бесплатно',
        'обман',
        'полиция',
        'радар',
    ]

    def clean_name(self):
        name = self.cleaned_data['name']

        # Проверка наличия запрещенных слов в названии
        for word in self.banned_words:
            if word.lower() in name.lower():
                raise forms.ValidationError(f'Название содержит запрещенное слово "{word}".')

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')

        # Проверка наличия запрещенных слов в описании
        for word in self.banned_words:
            if word.lower() in description.lower():
                raise forms.ValidationError(f'Описание содержит запрещенное слово "{word}".')

        return description