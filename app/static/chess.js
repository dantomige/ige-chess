const boardDiv = document.getElementById("board");
const initialBoard = [
    ["♜","♞","♝","♛","♚","♝","♞","♜"],
    ["♟","♟","♟","♟","♟","♟","♟","♟"],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["♙","♙","♙","♙","♙","♙","♙","♙"],
    ["♖","♘","♗","♕","♔","♗","♘","♖"]
];

for(let r=0;r<8;r++){
    for(let c=0;c<8;c++){
        const cell = document.createElement("div");
        cell.className = `cell ${(r+c)%2==0 ? "white":"black"}`;
        cell.textContent = initialBoard[r][c];
        boardDiv.appendChild(cell);
    }
}
