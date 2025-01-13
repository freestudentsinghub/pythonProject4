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

        for word in self.banned_words:
            if word.lower() in name.lower():
                raise forms.ValidationError(f'Название содержит запрещенное слово "{word}".')

        return name

    def clean_description(self):
        description = self.cleaned_data.get('description', '')

        for word in self.banned_words:
            if word.lower() in description.lower():
                raise forms.ValidationError(f'Описание содержит запрещенное слово "{word}".')

        return description

    def clean_cost(self):
        cost = self.cleaned_data.get('cost')

        if cost is not None and cost < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")

        return cost
