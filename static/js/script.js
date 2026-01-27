document.getElementById('togglePassword');

togglePassword.addEventListener('click', function (e) {
    const passwordField = document.getElementById('id_password');
    const type = passwordField.getAttribute('type') === 'password' ? 'text' : 'password';
    passwordField.setAttribute('type', type);
    this.classList.toggle('fa-eye-slash');
});
document.getElementById('createMealPlanForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const date = document.getElementById('date').value;
    if (date) {
        window.location.href = '/booking/' + date + '/';
    }
});