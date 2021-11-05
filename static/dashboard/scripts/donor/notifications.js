const template = (title, message, date) => `    
      <div class="bg-light-blue-lite p-4 rounded-10 mb-3">
        <p class="mb-0" style="font-weight: 500">
          ${title}
        </p>
        <p class="mb-0">
          ${message}
        </p>
        <p class="mb-0">
          Received: ${new Date(date).toLocaleString("id-ID")}
        </p>
      </div>
    `;
fetch("/dashboard-donor/api/notifications")
  .then((res) => res.json())
  .then((items) => {
    let inner = "";
    items.forEach((item) => {
      inner += template(
        item.fields.title,
        item.fields.message,
        item.fields.timestamp
      );
    });
    document.getElementById("notifications").innerHTML = inner;
  });
setInterval(() => {
  fetch("/dashboard-donor/api/notifications")
    .then((res) => res.json())
    .then((items) => {
      let inner = "";
      items.forEach((item) => {
        inner += template(
          item.fields.title,
          item.fields.message,
          item.fields.timestamp
        );
      });
      document.getElementById("notifications").innerHTML = inner;
    });
}, 10000);