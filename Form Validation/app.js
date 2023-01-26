const submit = document.getElementById('submit')

document.getElementById('name').addEventListener('keyup', validateName)
document.getElementById('zip').addEventListener('keyup', validateZip)
document.getElementById('email').addEventListener('keyup', validateEmail)
document.getElementById('phone').addEventListener('keyup', validatePhone)


function validateName() {
    const name = document.getElementById('name')
    const re = /^[A-Za-z]{3,9}$/;

    if(!re.test(name.value)) {
        name.classList.add('is-invalid')
        submit.disabled = true;
    } else {
        name.classList.remove('is-invalid')
        submit.disabled = false;
    }
}


function validateZip() {
    const zip = document.getElementById('zip')
    const re = /^[0-9]{6}(-[0-9]{4})?$/;

    if(!re.test(zip.value)) {
        zip.classList.add('is-invalid')
        submit.disabled = true;
    } else {
        zip.classList.remove('is-invalid')
        submit.disabled = false;
    }
}


function validateEmail() {
    const email = document.getElementById('email')
    const re = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    // const re = /^([a-zA-Z0-9_-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$/;

    if(!re.test(email.value)) {
        email.classList.add('is-invalid')
        submit.disabled = true;
    } else {
        email.classList.remove('is-invalid')
        submit.disabled = false;
    }
}


function validatePhone() {
    const phone = document.getElementById('phone')
    const re = /^\(?\d{3}\)?[-. ]?\d{3}[-. ]?\d{4}$/;

    if(!re.test(phone.value)) {
        phone.classList.add('is-invalid')
        submit.disabled = true;
    } else {
        phone.classList.remove('is-invalid')
        submit.disabled = false;
    }
}