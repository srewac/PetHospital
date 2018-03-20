from Disease.models import Disease, SubDisease


def get_all_diseases():
    disease_all = {}
    diseases = Disease.objects.all()
    for disease in diseases:
        disease_all[disease.name] = []
        sub_diseases = disease.subdisease_set.all()
        for sub_disease in sub_diseases:
            disease_all[disease.name].append(sub_disease)
    return disease_all
