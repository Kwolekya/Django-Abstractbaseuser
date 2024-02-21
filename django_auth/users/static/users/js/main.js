let btnAlert = document.querySelector('#dismiss-alert');

function closeAlert() {
  if (btnAlert){
    btnAlert.setAttribute('style', 'display:none;');
  }
}

setTimeout(closeAlert, 2500);

document.querySelector('.menu-btn').addEventListener("click", function(){
  document.querySelector('.sidebar').classList.toggle("active");
});



//for (let i = 0; i < btnSeat.length; i++) {
//  const seat = btnSeat[i];
//  seat.addEventListener('click', (()=> {
//    const seatNumber = seat.innerText;
//    console.log("Clicked Seat Number", seatNumber); 
//  }))
//}


// create a function that reserves a seat.
/*
const reserveSeat = async (event) => {
  event.preventDefault();
  let seat = event.target;
  const seatNumber = seat.innerText;
  const movie = document.querySelector('.seats').dataset.movie;
  const quantity = 1;
  const price = parseFloat(document.querySelector('.seats').dataset.price.replace(',', ''));
  const amount = Math.round(quantity * price)
  console.log(seatNumber, movie, price, amount);

 /* // fetch all seats to access each seat number's primary key.
  await fetch('/dashboard/seats/')
  .then((response) => {
    return response.json();
  }).then((seats) => {
    console.log(seats);
  })
*/

/*
  const data = {
    "seatNumber": "seatNumber",
    "movie": "movie",
    "quantity": 1,
    "price": price,
    "amount": amount
  };

  const options = {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify(data)
  };
  
  await fetch('1/book-seat/', options)
  .then((response) => {
    if (!response.ok) {
      throw Error(response.status);
     }
    return response.json()
  })
  .then((data) => {
    console.log("data:", data);
    location.reload();
  }) 
}

// select all buttons with a class of seat-number and iterate over them with a for loop.
let btnSeat = document.querySelectorAll('#seat-number');

for (let i = 0; i < btnSeat.length; i++) {
  btnSeat[i].addEventListener('click', reserveSeat);  
}






 
  




 function bookSeat(seatId, movie){
  console.log('SeatId:', seatId, 'Movie:', movie);
  let url = '/book-seat/'

  fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken
    },
    body: JSON.stringify({
      "seatId": seatId,
      "movie": movie
    })
  })
  .then((response) => {
    return response.json()
  })
  .then((data) => {
    console.log("data:", data);
    location.reload();
  })
}

function showAlert(message, className) {
  const div = document.createElement('div');
  div.className = `alert-msg ${className}`;
  div.appendChild(document.createTextNode(message));
  const hall = document.querySelector('.hall');
  const trailer = document.querySelector('.trailer');
  hall.insertBefore(div, trailer);
}
*/
