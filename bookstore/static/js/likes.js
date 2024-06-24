let likeButtons = document.getElementsByClassName('like-btn');

function getCookieValue(name) 
{
    const regex = new RegExp(`(^| )${name}=([^;]+)`)
    const match = document.cookie.match(regex)
    if (match) {
        return match[2]
    }
}

for (button of likeButtons) {
    button.addEventListener('click', (e) => {
        e.preventDefault();
        let id = e.target.getAttribute('data-id');
        console.log(`Pressed button with id ${id}`);
        var xhttp = new XMLHttpRequest();
        if (e.target.classList.contains('liked')) {
            xhttp.open("DELETE", `http://127.0.0.1:8000/api/likes/${id}/`);
            xhttp.setRequestHeader('Content-Type', 'application/json');
            xhttp.setRequestHeader('X-CSRFToken', getCookieValue('csrftoken'))
            xhttp.withCredentials = true;
            xhttp.send()
        } else {
            xhttp.open("POST", `http://127.0.0.1:8000/api/likes/`);
            let params = {'book': id}
            xhttp.setRequestHeader('Content-Type', 'application/json');
            xhttp.setRequestHeader('X-CSRFToken', getCookieValue('csrftoken'))
            xhttp.withCredentials = true;
            xhttp.send(JSON.stringify(params));
        }
        console.log(xhttp.responseText);
        e.target.classList.toggle('liked');
    })
}