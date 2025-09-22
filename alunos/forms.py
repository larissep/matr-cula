from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }

    def clean(self):
        cleaned_data = super().clean()
        instance = self.instance

        # Validar campos únicos
        for field in ['cpf', 'rg', 'email', 'numero_matricula']:
            value = cleaned_data.get(field)
            if value:
                qs = Aluno.objects.filter(**{field: value})
                if instance:
                    qs = qs.exclude(pk=instance.pk)
                if qs.exists():
                    self.add_error(field, f"Já existe um aluno com este {field}.")

        return cleaned_data
