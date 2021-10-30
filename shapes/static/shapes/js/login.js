const loginForm = document.querySelector('#login-form');
const usernameInput = document.querySelector('#id_username');
const passwordInput = document.querySelector('#id_password');
const formErrors = document.querySelector('#form-errors');
const loginBtn = document.querySelector('#login-btn');
const token = document.querySelector('input[name="csrfmiddlewaretoken"]').value;


async function login() {
    loginBtn.innerHTML = '<i class="fas fa-spinner spinning"></i>';
    loginBtn.style.pointerEvents = 'none';

    const response = await fetch('/api/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': token,
        },
        body: JSON.stringify({
            'username': usernameInput.value,
            'password': passwordInput.value 
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
        loginBtn.innerHTML = 'Try again';
        loginBtn.style.pointerEvents = 'all';
    }
}

loginForm.addEventListener('submit', event => {
    event.preventDefault();
    login();
})