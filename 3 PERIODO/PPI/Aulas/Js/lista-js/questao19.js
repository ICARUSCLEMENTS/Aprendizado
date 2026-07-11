function fatorial(n) {
  let resultado = 1;
  for (let i = 2; i <= n; i++) resultado *= i;
  return resultado;
}

function fatorialRecursivo(n) {
  if (n <= 1) return 1;
  return n * fatorialRecursivo(n - 1);
}

console.log("Fatorial 5 =", fatorial(5), fatorialRecursivo(5));
console.log("Fatorial 10 =", fatorial(10), fatorialRecursivo(10));
