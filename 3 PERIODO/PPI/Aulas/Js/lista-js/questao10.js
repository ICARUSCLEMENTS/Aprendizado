const prompt = require("prompt-sync")();

let a = parseFloat(prompt("Digite o primeiro número: "));
let b = parseFloat(prompt("Digite o segundo número: "));
let c = parseFloat(prompt("Digite o terceiro número: "));

let maior;
if (a >= b && a >= c) maior = a;
else if (b >= a && b >= c) maior = b;
else maior = c;

console.log("Maior número:", maior);
