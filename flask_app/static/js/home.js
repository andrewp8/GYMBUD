const apiKey = 'YOUR_API_KEY';


var recipe_display = document.querySelector("#recipe_display")
var recipe_input = document.querySelector("#recipe_input")
var recipe_input_btn = document.querySelector("#recipe_input_btn")
recipe_input_btn.addEventListener("click", (event) => {
  event.preventDefault();

  var encodeInput = recipe_input.value.replace(/\s/g, "%20");
  console.log(encodeInput);

  var apiUrl = `https://edamam-recipe-search.p.rapidapi.com/search?q=${encodeInput}`

  const options = {
    method: 'GET',
    headers: {
      'X-RapidAPI-Key': apiKey,
      'X-RapidAPI-Host': 'edamam-recipe-search.p.rapidapi.com'
    }
  };

  fetch(apiUrl, options)
    .then(response => response.json())
    .then(response => {
      console.log(response);

      var recipe_list = response['hits']
      // var video_url = video_list[0]['url']


      for (var i = 0; i < recipe_list.length; i++) {
        recipe_display.innerHTML += `
        <br>
        <img class="recipe_img" src="${recipe_list[i]['recipe']['image']}" alt="recipe_list[i]['recipe']['label']" >
        <p>Label: ${recipe_list[i]['recipe']['label']}</p>
        <p>Calories: ${recipe_list[i]['recipe']['calories'].toFixed(2)}</p>
        <p>Ingredients:</p>
        `
        for (var y = 0; y < recipe_list[i]['recipe']['ingredients'].length; y++) {
          recipe_display.innerHTML += `
          <li>Ingredients: ${recipe_list[i]['recipe']['ingredients'][y]['text']}</li>
          `
        }
      }
    })
    .catch(err => console.error(err));
})





var video_display = document.querySelector("#video_display")
var video_input = document.querySelector("#video_input")
var video_input_btn = document.querySelector("#video_input_btn")
video_input_btn.addEventListener("click", (event) => {
  event.preventDefault();

  //? replace empty space with %20 to use in URL
  var encodeInput = video_input.value.replace(/\s/g, "%20");
  console.log(encodeInput);

  var apiUrl = `https://youtube-search-results.p.rapidapi.com/youtube-search/?q=${encodeInput}`

  const options = {
    method: 'GET',
    headers: {
      'X-RapidAPI-Key': apiKey,
      'X-RapidAPI-Host': 'youtube-search-results.p.rapidapi.com'
    }
  };

  fetch(apiUrl, options)
    .then(response => response.json())
    .then(response => {
      var video_list = response.items
      console.log(video_list[0]['url'])
      var video_url = video_list[0]['url']

      // const videoElement = document.createElement("video");
      // videoElement.src = video_url;
      // videoElement.controls = true;
      // video_display.appendChild(videoElement);

      for (var i = 0; i < video_list.length; i++) {
        video_display.innerHTML += `
        <video src="${video_list[i]['url']}" controls></video>
        <p>${video_list[i]['title']}</p>
        <p>Views: ${video_list[i]['views']}</p>
        <br>
        `
      }
    })
    .catch(err => console.error(err));

})
