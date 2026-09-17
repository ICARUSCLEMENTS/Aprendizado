import { useState } from 'react'
import CampoTexto from './CampoTexto'
import Livro from './Livro'
import './FormularioLivro.css'

function FormularioLivro() {
  const [titulo, setTitulo] = useState('')
  const [autor, setAutor] = useState('')
  const [ano, setAno] = useState('')
  const [genero, setGenero] = useState('')

  const [livros, setLivros] = useState([])

  function handleSubmit(evento) {
    evento.preventDefault()

    const novoLivro = {id: Date.now, titulo, autor, ano, genero }
    setLivros([...livros, novoLivro])

    setTitulo('')
    setAutor('')
    setAno('')
    setGenero('')
  }

  return (
    <section className="formulario-livro">
      <h1>Cadastro de Livro</h1>

      <form onSubmit={handleSubmit}>
        <CampoTexto
          label="Título"
          name="titulo"
          value={titulo}
          onChange={(evento) => setTitulo(evento.target.value)}
          placeholder="Ex: Harry Potter"
        />

        <CampoTexto
          label="Autor"
          name="autor"
          value={autor}
          onChange={(evento) => setAutor(evento.target.value)}
          placeholder="Ex: Machado de Assis"
        />

        <CampoTexto
          label="Ano de Publicação"
          name="ano"
          type="date"
          value={ano}
          onChange={(evento) => setAno(evento.target.value)}
          placeholder="DD/MM/AAAA"
        />

        <CampoTexto
          label="Gênero"
          name="genero"
          value={genero}
          onChange={(evento) => setGenero(evento.target.value)}
          placeholder="Ex: Fantasia"
        />

        <button type="submit">Cadastrar</button>
      </form>

      <div className="formulario-livro-lista">
        <h2>Livros cadastrados</h2>

        {livros.length === 0 && <p>Nenhum Livro cadastrado ainda.</p>}

        <ul>
          {livros.map((livro) => (
            <Livro key={livro.id} livro={livro} />
          ))}
        </ul>
      </div>
    </section>
  )
}


export default FormularioLivro;
