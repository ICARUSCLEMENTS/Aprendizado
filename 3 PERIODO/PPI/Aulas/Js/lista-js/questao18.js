const ehPrimo = (num) => {
  if (num < 2) return false;
  for (let i = 2; i <= Math.sqrt(num); i++) {
    if (num % i === 0) return false;
  }
  return true;
};

for (let i = 2; i <= 50; i++) {
  if (ehPrimo(i)) console.log(i);
};
