document.addEventListener("DOMContentLoaded", function() {
    fetch('/api/passengers')
        .then(response => response.json())
        .then(data => {
            const content = document.getElementById('content');
            let html = '<h2>Passengers</h2><ul>';
            data.forEach(passenger => {
                html += `<li>${passenger.surname}, ${passenger.name}</li>`;
            });
            html += '</ul>';
            content.innerHTML = html;
        })
        .catch(error => console.error('Error fetching passengers:', error));
});
