function fetchMessage() {
  fetch('/api/greet')
    .then(res => res.json())
    .then(data => {
      document.getElementById('message').innerText = data.message;
    });
}
