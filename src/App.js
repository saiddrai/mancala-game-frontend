import "./App.css";
import { useEffect, useState } from "react";
import Modal from "./Modal";
import axios from "axios";
import { parse, stringify, toJSON, fromJSON } from "flatted";
import Navbar from "./Navbar";

function App() {
  const { parse, stringify, toJSON, fromJSON } = require("flatted");

  const [player1, setPlayer1] = useState({
    A: 4,
    B: 4,
    C: 4,
    D: 4,
    E: 4,
    F: 4,
  });
  const [player2, setPlayer2] = useState({
    G: 4,
    H: 4,
    I: 4,
    J: 4,
    K: 4,
    L: 4,
  });

  const [store1, setStore1] = useState(0);
  const [store2, setStore2] = useState(0);

  const [turn, setTurn] = useState(1);

  const [gameOver, setGameOver] = useState(false);

  const [winner, setWinner] = useState(0);

  useEffect(() => {}, []);

  const onPlay = (fosse) => {
    const data = {
      player: turn,
      fosse: fosse,
      player1: player1,
      player2: player2,
      store1: store1,
      store2: store2,
      gameOver: gameOver,
      winner: winner,
    };
    console.log(fosse);
    axios
      .post("http://localhost:5000/mancala", {
        player: turn,
        fosse: fosse,
        player1: player1,
        player2: player2,
        store1: store1,
        store2: store2,
        gameOver: gameOver,
        winner: winner,
      })
      .then((response) => {})
      .catch((error) => {
        console.log(error);
      });
  };

  const playerSideStyle = "flex space-x-2";
  const fosseStyle =
    "py-4 px-6 rounded-full border-2 border-black my-2  bg-darkwood ";
  const storeStyle =
    fosseStyle + "bg-darkwood text-white h-36 flex items-center";
  return (
    <div className="  h-screen p-32 bg-primary  ">
      <Navbar />
      <div className="bg-darkwood flex rounded-xl pr-2 pb-2 h-56 w-[60%] m-auto ">
        <div className=" bg-lightwood rounded-xl px-4 py-2  m-auto flex flex-row items-center justify-between  w-full h-full">
          <div className={` ${storeStyle} mb-10 `}>{store1}</div>
          <div className="h-full flex flex-col  items-center justify-between  ">
            <div className="flex flex-row ">
              <ul className="space-x-2 flex flex-row">
                {Object.keys(player1).map((fosse, i) => {
                  return (
                    <li key={i}>
                      <button
                        onClick={() => onPlay(fosse)}
                        key={i}
                        className={fosseStyle}
                      >
                        {player1[fosse]}
                      </button>
                    </li>
                  );
                })}
              </ul>
            </div>
            <div className="flex flex-row ">
              <ul className="space-x-2 flex flex-row ">
                {Object.keys(player2).map((fosse, i) => {
                  return (
                    <li key={i}>
                      <button
                        onClick={() => onPlay(fosse)}
                        key={i}
                        className={fosseStyle}
                      >
                        {player2[fosse]}
                      </button>
                    </li>
                  );
                })}
              </ul>
            </div>
          </div>
          <div className={` ${storeStyle} mt-10 `}>{store2} </div>
        </div>
      </div>
      <Modal />
    </div>
  );
}

export default App;
