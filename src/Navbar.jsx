import React from "react";
import logo from "./assets/mancala.png";
import ModalMode from "./ModalMode";

function Navbar() {
  const onClick = () => {};
  return (
    <div className="flex flex-row">
      <img src={logo} />

      <button> Mode </button>
      <ModalMode />
    </div>
  );
}

export default Navbar;
