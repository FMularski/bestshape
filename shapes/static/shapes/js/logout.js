const logoutBtn = document.querySelector('.btn-danger');
const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;


async function logout() {
    logoutBtn.style.pointerEvents = 'none';

    const response = await fetch('/api/logout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token
        }
    });

    if (response.status == 200) {
        location.href = '/login/';
    }
}


logoutBtn.addEventListener('click', logout);