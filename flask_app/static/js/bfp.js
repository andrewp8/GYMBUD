const apiKey = 'YOUR_API_KEY';



var myForm = document.querySelector("#myForm")
const bfp_results = document.querySelector('#bfp_results')

myForm.onsubmit = function (event) {
  event.preventDefault()

  var weight = document.getElementById("weight").value;
  var height = document.getElementById("height").value;
  var age = document.getElementById("age").value;
  var gender;
  var radioButtons = document.querySelectorAll('input[name="gender"]');
  radioButtons.forEach((button) => {
    if (button.checked) {
      gender = button.value;
    }
  });
  var form = new FormData(myForm)
  var user_id = document.querySelector('#user_id').value


  const apiUrl = `https://mega-fitness-calculator1.p.rapidapi.com/bfp?weight=${weight}&height=${height}&age=${age}&gender=${gender}`;
  fetch(apiUrl, {
    method: 'GET',
    headers: {
      'X-RapidAPI-Key': apiKey,
      'X-RapidAPI-Host': 'mega-fitness-calculator1.p.rapidapi.com'
    },
  })
    .then((response) => {
      // ? because code was wrapped inside a {}
      // ! return is required
      // * no need to return if >>> .then((response) => response.json)
      return response.json()
    })
    .then((data) => {
      var bfp = data.info['bfp'].toFixed(2);

      // Get data from Promise's result
      bfp_results.innerHTML = `
        <p>Your BFP: ${data.info['bfp'].toFixed(2)}%</p>
        <br>
        <p>Weight: ${weight} kg</p>
        <p>Height: ${height} cm</p>
        <p>Age: ${age} years old</p>
        <p>Gender: ${gender.charAt(0).toUpperCase() + gender.slice(1)}</p>
        `

      // Set up a post request and send the form data
      // ? add the value of bfp to the form first
      form.append('bfp', bfp)
      fetch(`http://127.0.0.1:5001/bfp/${user_id}`, { method: 'POST', body: form })
        .then(response => response.json())
        .then(data => console.log(data))
    })
    .catch((error) => console.error(error));
}






