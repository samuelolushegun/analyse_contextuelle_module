import { Routes, Route, Link } from 'react-router-dom';
import SwotPage from './modules/analyse_contextuelle/pages/SwotPage';

function App() {
  return (
    <div>
      <nav>
        <Link to="/swot">SWOT</Link>
        {/* À terme : PESTEL, Objectives, etc. */}
      </nav>
      <main>
        <Routes>
          <Route path="/swot" element={<SwotPage />} />
          {/* <Route path="/pestel" element={<PestelPage />} /> */}
        </Routes>
      </main>
    </div>
  );
}

export default App;
