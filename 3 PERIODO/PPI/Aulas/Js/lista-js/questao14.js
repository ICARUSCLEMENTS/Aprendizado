let notas = [7.5, 8.0, 6.5, 9.0, 5.5, 7.0, 8.5];
let somaNotas = 0;

for (let n of notas) somaNotas += n;

let media = somaNotas / notas.length;

console.log("Média =", media.toFixed(1));

let acima = 0;

for (let n of notas) if (n > media) acima++;

console.log("Alunos acima da média:", acima);
