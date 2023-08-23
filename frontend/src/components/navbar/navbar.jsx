import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import 'bootstrap/dist/css/bootstrap.min.css'
import './navbar.css'

export default function NavBar() {
  return (
    <Navbar collapseOnSelect expand="lg" className="bg-body-tertiary" data-bs-theme="dark">
      <Container>
        <Navbar.Brand href="/">Loja</Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="ms-auto">
            <NavDropdown title="Categorias" id="collapsible-nav-dropdown" align="end">
              <NavDropdown.Item href="/croches">Crochês</NavDropdown.Item>
              <NavDropdown.Item href="/cosmeticos">Cosméticos em pronta entrega</NavDropdown.Item>
              <NavDropdown.Item href="/revistas">Revistas para encomendas</NavDropdown.Item>
            </NavDropdown>
            <Nav.Link href='/login'>Login</Nav.Link>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}