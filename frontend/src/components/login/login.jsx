import { React, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';


export default function Login() {
  const [email, setEmail] = useState("")
  const [senha, setSenha] = useState("")
  
  const navigate = useNavigate();
  
  async function handleLogin() {
    const payload = {
      method: 'POST',
      headers: {"Content-type": "application/json;charset=UTF-8"},
      body:JSON.stringify({
        email: email,
        senha: senha
      })
    }
    const response = await fetch("http://localhost:8000/Usuarios/login", payload)
    if (response.ok){
      const data = await response.json()
      sessionStorage.setItem("userData", JSON.stringify(data))
      navigate('/')
    }
    else{
      alert("Email e/ou senha errados")
    }
  }

  return(
    <div>
      <Form>
        <Form.Group className='mb-3'>
          <Form.Label>Email:</Form.Label>
          <Form.Control type='email' placeholder='Digite seu email' value={email} onChange={e => setEmail(e.target.value)} />
        </Form.Group>
        <Form.Group className='mb-3'>
          <Form.Label>Senha:</Form.Label>
          <Form.Control type='password' placeholder='Digite sua senha' value={senha} onChange={e => setSenha(e.target.value)} />
        </Form.Group>
        <Button variant='primary' onClick={handleLogin}>Login</Button>
      </Form>
    </div>
  );
}