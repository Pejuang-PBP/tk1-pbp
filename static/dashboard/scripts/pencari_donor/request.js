const initializeInformationFields = () => {
  document.getElementById("request-information").innerHTML = `
    <div class="form-group mb-2">
      <label>Nama Pasien</label>
      <input type="text" class="form-control" id="nama_pasien" disabled />
    </div>
    <div class="form-group mb-3">
      <label>NIK</label>
      <input type="text" class="form-control" id="nik" disabled />
    </div>
    <div class="form-group mb-3">
      <label>Nomor Telepon</label>
      <input type="text" class="form-control" id="nomor_telepon" disabled />
    </div>
    <div class="row">
      <div class="col-sm-6">
        <div class="form-group">
          <label>Golongan Darah</label>
          <input
            type="text"
            class="form-control"
            id="golongan_darah"
            disabled
          />
        </div>
      </div>
      <div class="col-sm-6">
        <div class="form-group">
          <label>Rhesus</label>
          <input type="text" class="form-control" id="rhesus" disabled />
        </div>
      </div>
    </div>
  `;

  document.getElementById("request-button-container").classList.add("d-flex");
  document
    .getElementById("request-button-container")
    .classList.remove("d-none");
  document.getElementById("create-button-container").classList.add("d-none");
  document.getElementById("create-button-container").classList.remove("d-flex");
};

const resetInformationFields = () => {
  document.getElementById("request-information").innerHTML =
    "Anda belum memiliki request yang aktif. Silahkan membuat request baru dengan mengklik tombol dibawah.";

  document.getElementById("create-button-container").classList.add("d-flex");
  document.getElementById("create-button-container").classList.remove("d-none");
  document.getElementById("request-button-container").classList.add("d-none");
  document
    .getElementById("request-button-container")
    .classList.remove("d-flex");
};

const setFields = (item) => {
  const nama_pasien = document.getElementById("nama_pasien");
  const nik = document.getElementById("nik");
  const nomor_telepon = document.getElementById("nomor_telepon");
  const rhesus = document.getElementById("rhesus");
  const golongan_darah = document.getElementById("golongan_darah");

  nama_pasien.setAttribute("value", item.fields.nama);
  nik.setAttribute("value", item.fields.nomor_induk);
  nomor_telepon.setAttribute("value", item.fields.nomor_hp);
  golongan_darah.setAttribute("value", item.fields.golongan_darah);
  rhesus.setAttribute("value", item.fields.rhesus);
};

const updateRequest = () => {
  fetch("/dashboard-pencari/api/request")
    .then((res) => res.json())
    .then((data) => {
      if (data.length) {
        const item = data[0];

        initializeInformationFields();
        setFields(item);

        document.addEventListener("delete:request", (e) => {
          fetch(`/dashboard-pencari/api/request?id=${item.pk}`, {
            method: "DELETE",
          }).then(() => {
            updateRequest();
          });
        });

        document.getElementById("request-aktif").style = "display: block;";
      } else {
        resetInformationFields();
        document.getElementById("request-aktif").style = "display: none;";
      }
    });
};

// Add a new event listener
document.addEventListener("update:request", (e) => {
  updateRequest();
});

// Emit event to update request
document.dispatchEvent(new CustomEvent("update:request"));
