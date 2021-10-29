const registerForm = document.querySelector('#register-form');
const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

const usernameInput = document.querySelector('#id_username');
const password1Input = document.querySelector('#id_password1');
const password2Input = document.querySelector('#id_password2');
const registerBtn = document.querySelector('#register-btn');

registerForm.addEventListener('submit', event => {
    event.preventDefault();
    registerBtn.innerHTML = '<i class="fas fa-spinner spinning"></i>';

    fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token,
            'X-Requested-With':'XMLHttpRequest'
        },
        body: JSON.stringify({
            'username': usernameInput.value,
            'password1': password1Input.value,
            'password2': password2Input.value
        })
    })
    .then(response => response.json())
    .then(responseJSON => {
        registerBtn.innerHTML = 'Register';
        console.log(responseJSON);
    });
})