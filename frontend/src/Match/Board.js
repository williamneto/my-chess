import { Container, Row, Col } from "react-bootstrap"
import "./styles/board.module.css"

const Board =  ({match, sendMove }) => {

    const renderBoard = board => {
        const letters = "abcdefgh"

        const rows = []
        for (var x = 0; x < 8; x++) {
            let currentLetter = letters[x]
            let columns = []
            for (var y = 0; y < 8; y++) {
                let house = `${currentLetter}${y+1}`
                columns.push(
                    <Col >
                        <b>
                            {house}
                        </b>
                        {board[house]}
                    </Col>
                )
            }

            rows.push(
                <Row>
                    {columns}
                </Row>
            )
        }

        return (
            <Container>
                {rows}
            </Container>
        )
    }

    return (
        <>
            {renderBoard(match.board)}
        </>
    )
}

export default Board