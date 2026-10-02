import './PokemonCard.css'

function PokemonCard(props) {
  return (
    <div className="card">
      <img className="foto" src={props.imagem} alt={props.nome} />
      <div className="informacoes">
      <span className="numero">#{props.numero}</span>
      <h3 className="nome">{props.nome}</h3>
      </div>
    </div>
  )
}

export default PokemonCard
