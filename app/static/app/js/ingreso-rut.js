function formatRut(rut) {
  var actual = rut.replace(/^0+/, "").replace(/[^\dkK]/g, "").toUpperCase();
  var sinPuntos = actual.replace(/\./g, "");
  var cuerpo = sinPuntos.slice(0, -1);
  var dv = sinPuntos.slice(-1);
  actual = cuerpo + "-" + dv;
  return actual;
}

function validarRut(rut) {
  if (!/^[0-9]+[-|‐]{1}[0-9kK]{1}$/.test(rut)) return false;
  var tmp = rut.split("-");
  var digv = tmp[1];
  var rut = tmp[0];
  if (digv == "K") digv = "k";
  return dv(rut) == digv;
}

function dv(T) {
  var M = 0,
    S = 1;
  for (; T; T = Math.floor(T / 10))
    S = (S + (T % 10) * (9 - (M++ % 6))) % 11;
  return S ? S - 1 : "k";
}

var rutInput = document.getElementById("rut");
rutInput.addEventListener("blur", function() {
  var rut = formatRut(this.value);
  this.value = rut;
  if (!validarRut(rut)) {
    alert("RUT inválido");
    this.value = "";
  }
});

rutInput.addEventListener("input", function(event) {
  this.value = this.value.replace(/[^0-9kK\-]/g, "");
  var maxLength = 12;
  var rut = this.value.replace(/\./g, "").replace(/\-/g, "");
  if (rut.length > maxLength) {
    this.value = this.value.substring(0, this.value.length - 1);
  }
  if (rut.length === maxLength) {
    this.value = rut.slice(0, -1) + "-" + rut.slice(-1).toUpperCase();
  }
});


  
