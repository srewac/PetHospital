from django import forms
from Disease.models import Disease, SubDisease


class QuestionCreateForm(forms.Form):
    DISEASES = []
    SUBDISEASES = []

    diseases = Disease.objects.all()
    for disease in diseases:
        DISEASES.append((str(disease.id), disease.name))

    sub_diseases = diseases[0].subdisease_set.all()
    for sub_disease in sub_diseases:
        SUBDISEASES.append((str(sub_disease.id), sub_disease.name))

    disease_selector = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control', 'onChange': "getSubDiseaseOptions(this.value, 'create')"}),
        choices=DISEASES)
    sub_disease_selector = forms.ChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices=SUBDISEASES)
