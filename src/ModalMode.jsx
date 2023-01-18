import React, { useState } from "react";

export default function ModalMode() {
  const [showModal, setShowModal] = useState(false);
  const [mode, setMode] = useState(false); // false = human vs ai

  const chooseMode = (modeSet) => {
    setShowModal(!showModal);
    setMode(modeSet);
  };
  return (
    <>
      <button
        className="bg-secondary text-primary  font-bold uppercase text-sm px-6 py-3 rounded shadow hover:shadow-lg outline-none focus:outline-none mr-1 mb-1 ease-linear transition-all duration-150"
        type="button"
        onClick={() => setShowModal(true)}
      >
        open
      </button>
      {showModal ? (
        <div className="flex justify-items-center">
          <div className="opacity-50 fixed inset-0 z-40 bg-black"></div>
          <div className="z-50 absolute m-auto bg-white rounded-lg  w-1/3 h-72 flex py-auto flex-col">
            <h1 className="text-lg font-bold text-center py-4 pt-8">
              {" "}
              Choose Game Mode !
            </h1>
            <button
              className="bg-white z-50 flex justify-items-center text-primary border-secondary border-[1px] shadow-xl font-bold uppercase text-sm px-6 py-2 h-10 hover:shadow-md rounded-md outline-none focus:outline-none mx-auto my-6  ease-linear transition-all duration-150"
              onClick={() => setShowModal(false)}
            >
              AI VS AI
            </button>
            <button
              className="bg-white z-50 flex justify-items-center text-primary border-secondary border-[1px] shadow-xl font-bold uppercase text-sm px-6 py-2 h-10 hover:shadow-md rounded-md outline-none focus:outline-none mx-auto my-6  ease-linear transition-all duration-150"
              onClick={() => setShowModal(false)}
            >
              HUMAN VS AI
            </button>
          </div>
        </div>
      ) : null}
    </>
  );
}
