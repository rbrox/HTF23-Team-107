document.getElementById("login-form").addEventListener("submit", function (e) {
    e.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // You can add basic client-side validation here if needed.

    // Simulate a successful login (replace with actual authentication logic)
    if (username === "user" && password === "password") {
        window.location.href = "index.html"; // Redirect to the user dashboard
    } else {
        document.getElementById("error-message").textContent = "Invalid username or password.";
    }
});
