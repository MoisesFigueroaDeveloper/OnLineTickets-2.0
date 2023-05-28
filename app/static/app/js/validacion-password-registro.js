function formatPassword(password) {
    var actual = password.replace(/\s+/g, "").toUpperCase();
    return actual;
  }
  
  function validarPassword(password) {
    if (!/^(?=.*\d).{8,}$/.test(password)) return false;
    return true;
  }
  
  var passwordInput = document.getElementById("password");
  passwordInput.addEventListener("blur", function() {
    var password = formatPassword(this.value);
    this.value = password;
    if (!validarPassword(password)) {
      alert("La contraseña debe tener al menos 8 caracteres y 1 número");
      this.value = "";
    }
  });
  