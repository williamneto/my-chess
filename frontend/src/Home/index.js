import { Container, Row, Col, Button } from "react-bootstrap"
import { API_HOST  } from "../config";
import axios from "axios"

const Home = () => {
  
  const newMatch = () => {
    axios.get(
      `${API_HOST}/matchs/new`
    ).then( response => {
      if (response.status === 200 ) {
        window.location.href = "/m/" + response.data.mid
      }
      console.log(response)
    }).catch(function (error) {
      // handle error
      console.log(error);
    })
  }

  return (
    <Container>
      <Row>
        <Col>
          <h6>Entrar em uma partida</h6>
          <input 
            type="text"
            placeholder="ID da partida"
          />
          <Button
            variant="dark"
          >
            Entrar
          </Button>
        </Col>
        <Col>
          <h6>Iniciar uma partida</h6>
          <Button
            variant="dark"
            onClick={ e => newMatch()}
          >
            Iniciar
          </Button>
        </Col>
      </Row>
      
    </Container>
  )
};
  
export default Home;
  