const prompt = require("prompt-sync")();

function calcularIMC(peso, altura) {
  return peso / (altura * altura);
}
function classificarIMC(imc) {
  if (imc < 18.5) return "Abaixo do peso";
  else if (imc < 25) return "Normal";
  else if (imc < 30) return "Sobrepeso";
  else return "Obesidade";
}

let peso = parseFloat(prompt("Digite o peso (kg): "));
let altura = parseFloat(prompt("Digite a altura (m): "));
let imc = calcularIMC(peso, altura);

console.log("IMC =", imc.toFixed(2), "-", classificarIMC(imc));
