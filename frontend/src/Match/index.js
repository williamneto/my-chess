import axios from "axios"
import { useEffect, useState } from "react"
import { Button, Container, Row, Col } from "react-bootstrap"
import { useParams } from "react-router-dom"
import useWebSocket from 'react-use-websocket';
import { API_HOST, WS_HOST } from "../config"
import Board from "./Board";

const Match = () => {
    const { mid } = useParams()
    const [match, setMatch] = useState(null)

    const [playerMove, setPlayerMove] = useState("")

    const [playerIp,setIP] = useState('');
    
    const getClientIp = async()=>{
        const res = await axios.get(
            'https://geolocation-db.com/json/'
        )
        setIP(res.data.IPv4)
    }
    useEffect( () => {
        getClientIp()
    }, [])

    useEffect( () => {
        if (playerIp){
            axios.post(
                `${API_HOST}/matchs/${mid}`,
                {
                    "player": playerIp
                }
            ).then( response => {
                if (response.status === 200) {
                    setMatch(
                        response.data
                    )
                }
            })
        }
    }, [playerIp])

    const handleIncomingMessage = m => {
        setMatch(
            JSON.parse(m.data)
        )
    }

    const socketUrl = `${WS_HOST}/match?match_id=${mid}&player=${playerIp}`
    const {
        sendMessage,
        sendJsonMessage,
        lastMessage,
        lastJsonMessage,
        readyState,
        getWebSocket,
      } = useWebSocket(socketUrl, {
        onOpen: () => sendMessage("{}"),
        onMessage: m => handleIncomingMessage(m),
        //Will attempt to reconnect on all close events, such as server shutting down
        shouldReconnect: (closeEvent) => true,
      });

    const sendMove = move => {
        console.log(match)
        let payload = {
            "mid": match.mid,
            "action": "player_move",
            "move": move,
            "player": match.player
        }

        sendMessage(
            JSON.stringify(
                payload
            )
        )
    }

    return (
        <Container>
            <h1>Partida</h1>
        
            <Container>
                { match && (
                    <>
                        <b>Player {match?.player + 1}</b>
                        {match?.board && <Board 
                            match={match}
                            sendMove={sendMove}
                        />}

                        <Row>
                            <Col>
                                { match.turn === match.player ? (
                                    <Row>
                                        <Col>
                                            <input
                                                type="text"
                                                placeholder="Jogada"
                                                value={playerMove}
                                                onChange={ e => setPlayerMove(e.target.value)}
                                            />
                                        </Col>
                                        <Col>
                                            <Button
                                                variant="dark"
                                                onClick={ e => sendMove(playerMove)}
                                            >
                                                Enviar
                                            </Button>
                                        </Col>
                                    </Row>
                                ) : (
                                    <Row>
                                        <Col>
                                            Aguardando outro jogador
                                        </Col>
                                    </Row>
                                )}
                            </Col>
                            <Col>
                                {match.moves.map( move => {
                                    return (
                                        <i> - {move} - </i>
                                    )
                                })}
                            </Col>
                        </Row>
                    </>
                )}
            </Container>
            
                        
        </Container>
    )
}

export default Match