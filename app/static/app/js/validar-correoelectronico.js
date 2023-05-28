function validarCorreoElectronico(correo) {
    const expresionRegular = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;
    return expresionRegular.test(correo);
  }
  
  // Ejemplo de uso:
  const correoValido = validarCorreoElectronico("ejemplo@ejemplo.com");
  console.log(correoValido); // true
  
  const correoInvalido = validarCorreoElectronico("ejemplo.com");
  console.log(correoInvalido); // false