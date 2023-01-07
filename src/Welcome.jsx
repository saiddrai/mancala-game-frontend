import React from "react";
import { Link } from "react-router-dom";
import logo from "./assets/mancala.png";
import board from "./assets/board.png";

function Welcome() {
  return (
    <div className="flex bg-[#050511] flex-col justify-start items-center space-y-10 py-20 h-screen">
      <img className="w-20 mx-auto" src={logo} alt="Welcome" />
      <h1>Welcome to Mancala</h1>
      <Link
        to="/play"
        className="py-2 px-8 w-fit bg-blue-500 hover:bg-blue-700 text-white font-bold rounded"
      >
        Play
      </Link>
      {/* <button>Play</button> */}

      <img className="w-1/4 mx-auto" src={board} alt="Welcome" />
    </div>
  );
}

export default Welcome;
