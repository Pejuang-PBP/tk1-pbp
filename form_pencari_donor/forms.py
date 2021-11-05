from django import forms
from .models import request_pencari_donor

ROLE_GENDER = [("Laki-laki", "Laki-Laki"), ("Perempuan", "Perempuan")]
RHESUS = [
    ("+", "+"),
    ("-", "-"),
]
BLOOD_TYPE_CHOICES = [
    ("A", "A"),
    ("B", "B"),
    ("AB", "AB"),
    ("O", "O"),
]
URGENCY = [
    ("LOW", "Low"),
    ("MEDIUM", "Medium"),
    ("HIGH", "High"),
]


def nik_validator(valid):
    if not valid.isdigit() or len(valid) != 16:
        raise forms.ValidationError("NIK harus terdiri dari 16 angka")


class request_pencari_donor_form(forms.ModelForm):
    nama = forms.CharField(label="Nama Lengkap")
    nama.widget.attrs.update({"class": "form-control"})

    nomor_induk = forms.CharField(label="NIK", validators=[nik_validator])
    nomor_induk.widget.attrs.update({"class": "form-control"})

    nomor_hp = forms.CharField(label="Nomor HP")
    nomor_hp.widget.attrs.update({"class": "form-control"})

    jenis_kelamin = forms.ChoiceField(choices=ROLE_GENDER, label="Jenis Kelamin")
    jenis_kelamin.widget.attrs.update({"class": "form-select"})

    tanggal_lahir = forms.DateField(
        widget=forms.DateTimeInput(attrs={"type": "date", "class": "form-control"})
    )

    tempat_lahir = forms.CharField(label="Tempat Lahir")
    tempat_lahir.widget.attrs.update({"class": "form-control"})

    alamat = forms.CharField(
        label="Alamat",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
    )

    golongan_darah = forms.ChoiceField(
        choices=BLOOD_TYPE_CHOICES, label="Golongan Darah"
    )
    golongan_darah.widget.attrs.update({"class": "form-select"})

    rhesus = forms.ChoiceField(choices=RHESUS, label="Rhesus")
    rhesus.widget.attrs.update({"class": "form-select"})

    tempat_rawat = forms.CharField(
        label="Nama Rumah Sakit Tempat anda dirawat?",
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 3}),
    )

    urgency = forms.ChoiceField(choices=URGENCY, label="Urgency")
    urgency.widget.attrs.update({"class": "form-select"})

    class Meta:
        model = request_pencari_donor
        exclude = ["user"]
