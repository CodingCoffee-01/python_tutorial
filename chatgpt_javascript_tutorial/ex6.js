const axios = require("axios");

axios.get("https://www.google.com")
  .then(response => {
    console.log(response.status);  // Output: 200
    console.log(response.data);    // Output: the HTML content of the Google homepage
  })
  .catch(error => {
    console.log(error);
  });