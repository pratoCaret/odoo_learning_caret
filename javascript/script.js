function validateForm() {
    const name = document.getElementById("name").value;
    const addr = document.getElementById("address").value;
    const email = document.getElementById("email").value;
    const pass = document.getElementById("password").value;
    const sub = document.getElementById("subject").value;
    const agree = document.getElementById("agree").checked;

    const nameErr = document.getElementById("name-error").textContent = "";
    const addrErr = document.getElementById("address-error").textContent = "";
    const emailErr = document.getElementById("email-error").textContent = "";
    const passErr = document.getElementById("password-error").textContent = "";
    const subErr = document.getElementById("subject-error").textContent = "";
    const agreeErr = document.getElementById("agree-error").textContent = "";

    let isValid = true;
    if (name === "" || /\d/.test(name)) {
        nameErr.textContent = "Please enter your name properly.";
        isValid = false;
    }
    if (addr === "") {
        addrErr.textContent = "Please enter your address.";
        isValid = false;
    }
    if (email === "" || !email.includes("@") || !email.includes(".")) {
        emailErr.textContent = "Please enter a valid email address.";
        isValid = false;
    }
    if (pass === "" || pass.length < 6) {
        passErr.textContent = "Please enter a password with at least 6 characters.";
        isValid = false;
    }
    if (sub === "") {
        subErr.textContent = "Please select your course.";
        isValid = false;
    }
    if (!agree) {
        agreeErr.textContent = "Please agree to the above information.";
        isValid = false;
    }
    if (isValid) {
        alert("Form submitted successfully!");
        return true;
    } else {
        return false; 
    }
}

function resetErrors() {
    document.getElementById("name-error").textContent = "";
    document.getElementById("address-error").textContent = "";
    document.getElementById("email-error").textContent = "";
    document.getElementById("password-error").textContent = "";
    document.getElementById("subject-error").textContent = "";
    document.getElementById("agree-error").textContent = "";
}