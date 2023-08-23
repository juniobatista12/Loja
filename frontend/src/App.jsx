import logo from './logo.svg';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import Index from './components/index/index';
import Login from './components/login/login';
import NavBar from './components/navbar/navbar';

function IndexRoute() {
  return(
    <div>
      <NavBar />
      <Index />
    </div>
  )
}

function LoginRoute(){
  return(
    <div>
      <NavBar />
      <Login />
    </div>
  )
}

function App() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={<IndexRoute />} />
        <Route path='/login' element={<LoginRoute />} />
      </Routes>
    </Router>
  );
}

export default App;
