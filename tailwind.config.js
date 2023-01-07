/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      // add a new color
      colors: {
        primary: "#050511",
        secondary: "#F6851B",
        darkwood: "#9A7E5B",
        lightwood: "#B09169",
      },
      // add an image as a background
      backgroundImage: (theme) => ({
        board: "url('/src/assets/board.png')",
        wood: "url('/src/assets/wood.jpg')",
      }),
    },
  },
  plugins: [],
};
