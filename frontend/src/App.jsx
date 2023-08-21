import logo from './logo.svg';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Index from './components/index/index'
import NavBar from './components/navbar/navbar';

function IndexRoute() {
  return(
    <div>
      <NavBar />
      <Index />
    </div>
  )
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<IndexRoute />} />
      </Routes>
    </Router>
  );
}

export default App;
