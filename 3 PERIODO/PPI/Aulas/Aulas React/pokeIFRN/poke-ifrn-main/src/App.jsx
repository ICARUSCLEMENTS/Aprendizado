import { useEffect, useState } from 'react'
import PokemonCard from './components/PokemonCard'
import './App.css'

// A API nao manda a imagem, mas o endereco dela e sempre o mesmo:
// so muda o numero do pokemon no final.
const SPRITES = 'https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork'

function App() {
  const [lista, setLista] = useState([])

  useEffect(() => {
    fetch('https://pokeapi.co/api/v2/pokemon?limit=40')
      .then((resposta) => resposta.json())
      .then((dados) => setLista(dados.results))
  }, [])

  return (
    <div className="container">
      <h1>pokeIFRN</h1>

      <div className="grade">
        {lista.map((pokemon) => {
          // a url e "https://pokeapi.co/api/v2/pokemon/1/",
          // entao o pedaco de numero 6 e o numero do pokemon
          const numero = pokemon.url.split('/')[6]

          return (
            <PokemonCard
              key={numero}
              nome={pokemon.name}
              numero={numero}
              imagem={`${SPRITES}/${numero}.png`}
            />
          )
        })}
      </div>
    </div>
  )
}

export default App
