const prompt = require("prompt-sync")();

let idade = parseInt(prompt("Digite sua idade: "));
let temCarteirinha = prompt("Tem carteirinha? (s/n): ") === "s";

if (idade <= 12) console.log("Ingresso: R$ 15,00");
else if (idade >= 13 && idade <= 25 && temCarteirinha) console.log("Ingresso: R$ 20,00");
else if (idade >= 26 && idade <= 59) console.log("Ingresso: R$ 30,00");
else console.log("Ingresso: R$ 15,00");
