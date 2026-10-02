import { Routes, Route, Link } from 'react-router-dom'
import Home from './paginas/Home'
import Sobre from './paginas/Sobre'
import Contato from './paginas/Contato'
import NaoEncontrada from './paginas/NaoEncontrada'

function App() {
  return (
    <div>
      <nav>
        <Link to="/">Home</Link>
        <Link to="/sobre">Sobre</Link>
        <Link to="/contato">Contato</Link>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/sobre" element={<Sobre />} />
        <Route path="/contato" element={<Contato />} />
        <Route path="*" element={<NaoEncontrada />} />
      </Routes>
    </div>
  )
}

export default App