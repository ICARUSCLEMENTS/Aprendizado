const prompt = require("prompt-sync")();

let nota = parseInt(prompt("Digite a nota (0-100): "));

if (nota >= 60) {
  console.log("Aprovado");
} else {
  console.log("Reprovado");
}
