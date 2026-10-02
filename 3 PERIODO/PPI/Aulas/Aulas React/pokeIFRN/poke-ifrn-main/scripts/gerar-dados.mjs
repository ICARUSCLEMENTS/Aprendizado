/**
 * Gera src/data/pokemons.json a partir da PokeAPI (https://pokeapi.co).
 *
 *   node scripts/gerar-dados.mjs        # 12 primeiros (padrao)
 *   node scripts/gerar-dados.mjs 151    # geracao 1 completa
 *
 * Guardamos os dados em arquivo para nao repetir requisicoes a cada carregamento
 * da pagina: a PokeAPI pede cache local na politica de uso justo, e a resposta
 * de /pokemon/{id} tem ~270 KB por causa da lista de golpes, da qual nao usamos nada.
 */
import { writeFile, mkdir } from 'node:fs/promises'

const total = Number(process.argv[2]) || 12
const destino = new URL('../src/data/pokemons.json', import.meta.url)

async function buscar(numero) {
  const resposta = await fetch(`https://pokeapi.co/api/v2/pokemon/${numero}`)
  if (!resposta.ok) throw new Error(`#${numero}: HTTP ${resposta.status}`)
  const p = await resposta.json()

  return {
    numero: p.id,
    nome: p.name,
    tipos: p.types.map((t) => t.type.name),
    imagem: p.sprites.other['official-artwork'].front_default,
    altura: p.height / 10, // a API devolve em decimetros
    peso: p.weight / 10, // a API devolve em hectogramas
    stats: Object.fromEntries(p.stats.map((s) => [s.stat.name, s.base_stat])),
  }
}

const lista = []
for (let numero = 1; numero <= total; numero++) {
  lista.push(await buscar(numero))
  process.stdout.write(`\r${numero}/${total}`)
}

await mkdir(new URL('../src/data/', import.meta.url), { recursive: true })
await writeFile(destino, JSON.stringify(lista, null, 2) + '\n')
console.log(`\n${lista.length} pokemon gravados em src/data/pokemons.json`)
