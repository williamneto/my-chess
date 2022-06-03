import { Outlet } from "react-router-dom";
import { Navbar, Container, Nav} from "react-bootstrap"

const Layout = () => {
  return (
    <>
      <Navbar>
        <Container>
          <Navbar.Brand href="/">
            my-chess
          </Navbar.Brand>

          <Navbar.Toggle aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav">
            <Nav className="me-auto">
              <Nav.Link href="/match"></Nav.Link>
              
            </Nav>
          </Navbar.Collapse>
        </Container>
      </Navbar>
      
      <Outlet />
    </>
  )
};

export default Layout;
