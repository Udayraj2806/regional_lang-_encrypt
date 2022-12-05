console.log("got into it");
const fs = require("fs");

function data() {
  fs.readFile("ciphertext.txt", function (err, data) {
    if (err) {
      return console.error(err);
    }
    console.log("Data read : " + data.toString());
  });
  return data.toString;
}
console.log("Hello");
document.getElementById("encrypted12").innerHTML = "Inserted";

// export { data };
