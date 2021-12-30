import django_filters

from .models import UTD


class FilterKota(django_filters.FilterSet):
    class Meta:
        model = UTD
        fields = "__all__"
        exclude = ["nama", "jamOperasi", "nomorTelepon", "alamat"]
