function validarEmail(email) {
    // Patrón para validar el formato del correo electrónico
    var patronEmail = /^[^@]+@[^@]+\.[a-zA-Z]{2,}$/;
    return patronEmail.test(email);
  }
  
  var emailInput = document.getElementById("email");
  emailInput.addEventListener("blur", function() {
    var email = this.value;
    if (!validarEmail(email)) {
      alert("Email inválido");
      this.value = "";
    }
  });
  