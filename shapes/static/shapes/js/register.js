const registerForm = document.querySelector('#register-form');
const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

const usernameInput = document.querySelector('#id_username');
const password1Input = document.querySelector('#id_password1');
const password2Input = document.querySelector('#id_password2');
const registerBtn = document.querySelector('#register-btn');
const formErrors = document.querySelector('#form-errors');

async function register() {
    registerBtn.innerHTML = '<i class="fas fa-spinner spinning"></i>';
    registerBtn.style.pointerEvents = 'none';

    const response = await fetch('/api/register/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token,
        },
        body: JSON.stringify({
            'username': usernameInput.value,
            'password1': password1Input.value,
            'password2': password2Input.value
        })
    });

    if (response.status == 200) {
        location.href = '/';
    } else {
        const errors = await response.json();        
        for(let field in errors) {
            formErrors.innerHTML += 
                '<span><b>' + field + ':</b></span>' + 
                '<p>' + errors[field].join('\n') + '</p>';
        }

        usernameInput.value = '';
        password1Input.value = '';
        password2Input.value = '';
        registerBtn.innerHTML = 'Try again';
        registerBtn.style.pointerEvents = 'all';
    }
}

registerForm.addEventListener('submit', event => {
    event.preventDefault();
    register();
})