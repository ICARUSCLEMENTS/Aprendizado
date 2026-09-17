// Componente que recebe um aluno via props e mostra os dados dele.
function Livro({ livro }) {
  return (
    <li className="livro">
      <p>{livro.titulo}</p>
      <p>{livro.autor}</p>
      <p>{livro.ano}</p>
      <p>{livro.genero}</p>
    </li>
  )
}

export default Livro;
