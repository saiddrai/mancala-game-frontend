import "./App.css";
import { useState } from "react";

function App() {
  const [player1, setPlayer1] = useState({
    A: 4,
    B: 4,
    C: 4,
    D: 4,
    E: 4,
    F: 4,
  });
  const [player2, setPlayer2] = useState({
    A: 4,
    B: 4,
    C: 4,
    D: 4,
    E: 4,
    F: 4,
  });

  const [store1, setStore1] = useState(0);
  const [store2, setStore2] = useState(0);

  const [turn, setTurn] = useState(1);

  const [gameOver, setGameOver] = useState(false);

  const [winner, setWinner] = useState(0);

  const onClick = (fosse) => {
    // send the fosse to the server
    // get the response of all the states
    // update the states
    fetch("http://localhost:5000/mancala", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        fosse: fosse,
        turn: turn,
        player1: player1,
        player2: player2,
        store1: store1,
        store2: store2,
      }),
    })
      .then((response) => response.json())
      .then((data) => {
        // update states
        setPlayer1(data.player1);
        setPlayer2(data.player2);
        // update stores
        setStore1(data.store1);
        setStore2(data.store2);
        // update turn
        setTurn(data.turn);
        // update game over
        setGameOver(data.gameOver);
        // update winner
        setWinner(data.winner);
      });
  };

  const playerSideStyle = "flex space-x-2";
  const fosseStyle =
    "py-4 px-6 rounded-full border-2 border-black my-2  bg-darkwood ";
  const storeStyle =
    fosseStyle + "bg-darkwood text-white h-36 flex items-center";
  return (
    <div className="  h-screen p-32 bg-primary  ">
      <div className="bg-darkwood flex rounded-xl pr-2 pb-2 h-56 w-[60%] m-auto ">
        <div className=" bg-lightwood rounded-xl px-4 py-2  m-auto flex flex-row items-center justify-between  w-full h-full">
          <div className={` ${storeStyle} mb-10 `}>{store1}</div>
          <div className="h-full flex flex-col  items-center justify-between  ">
            <div className="flex flex-col">
              <ul className={playerSideStyle}>
                {Object.values(player2).map((fosse) => (
                  <il>
                    <button className={fosseStyle}>{fosse}</button>
                  </il>
                ))}
              </ul>
            </div>
            <div className={playerSideStyle}>
              {Object.values(player1).map((fosse) => {
                return <button className={fosseStyle}>{fosse}</button>;
              })}
            </div>
          </div>
          <div className={` ${storeStyle} mt-10 `}>{store2} </div>
        </div>
      </div>
    </div>
  );
}

export default App;
