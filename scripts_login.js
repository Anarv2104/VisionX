document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault(); // Prevent form submission

    // Get username and password
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;

    // Validate username and password (you can add your own validation logic here)

    // Redirect to main index page if login is successful
    window.location.href = "base.html";
});
const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.querySelector('.container');

signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
});

signInButton.addEventListener('click', () => {
    container.classList.remove('right-panel-active');
});