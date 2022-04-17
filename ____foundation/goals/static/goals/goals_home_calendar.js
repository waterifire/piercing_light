const date = new Date()

const renderCalendar = () => {
  date.setDate(1);


  const months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
  ]

  month_number_in_months = date.getMonth()
  month_display = document.querySelector(".date_month")
  month_display.textContent = months[month_number_in_months]


  day_display = document.querySelector('.date p')
  day_display.textContent = date.toDateString()


  let days = ""

  const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0)
  const lastDayDate = lastDay.getDate()

  const firstDayIndex = date.getDay()
  const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0)
  const prevLastDayDate = prevLastDay.getDate()

  const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0)
  const lastDayIndexDate = lastDayIndex.getDay()
  const nextDays = 7 - lastDayIndexDate - 1;

  for(let x= firstDayIndex; x > 0; x--) {
    days += `<div class="prev-date">${prevLastDayDate-x + 1}</div>`;

  }

  const monthDays = document.querySelector('.days')
  for(let i = 1; i<= lastDayDate; i++) {
    if(i === new Date().getDate() && date.getMonth() === new Date().getMonth()){
      days += `<div class="today">${i}</div>`;
    } else {
      days += `<div>${i}</div>`
    }
  }



  for(let j=1; j<=nextDays; j++) {
    days += `<div class="next-date">${j}</div>`
  }
  monthDays.innerHTML = days;
}



var prevChoice = document.querySelector('.prev')
prevChoice.addEventListener('click', () => {
  date.setMonth(date.getMonth() - 1)
  renderCalendar()
})

var prevChoice = document.querySelector('.next')
prevChoice.addEventListener('click', () => {
  date.setMonth(date.getMonth() + 1)
  renderCalendar()
})

renderCalendar()
