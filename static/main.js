console.log("Hello from main.js!");

document.getElementById("my-form").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent the default form submission behavior
  var formData = new FormData(this); // Get the form data as a FormData object
  // Send a POST request to the Flask or Django backend using fetch()
  fetch("/predict", {
      method: "POST",
      body: formData
  })
  .then(function(response) {
    // console.log(response);
      return response.text(); // Parse the response as text
  })
  .then(function(result) {
      document.getElementById("output").textContent = result; // Display the result
      console.log(result);
  })
  .catch(function(error) {
      console.error(error); // Log any errors
  });
});

