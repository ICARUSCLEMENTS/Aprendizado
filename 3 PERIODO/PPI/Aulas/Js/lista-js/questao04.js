// O readline é deveras muito ruim, pra não dizer outra coisa.
const prompt = require("prompt-sync")();

let nome = prompt("Digite seu nome: ");
let idade = prompt("Digite sua idade: ")

console.log(`Olá ${nome}! Você tem ${idade} anos.`)