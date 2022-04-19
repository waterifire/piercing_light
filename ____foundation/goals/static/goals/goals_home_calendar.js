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

  checkedDays = []
  const monthDays = document.querySelector('.days')
  for(let i = 1; i<= lastDayDate; i++) {
    if(i === new Date().getDate() && date.getMonth() === new Date().getMonth()){
      days += `<div class="today">${i}</div>`;
      checkedDays.push(i)
    } else {
      days += `<div>${i}</div>`
      checkedDays.push(i)
    }
  }

  for(let j=1; j<=nextDays; j++) {
    days += `<div class="next-date">${j}</div>`
    }
    monthDays.innerHTML = days;


// Django here ################################
    const checkedMonth = months[month_number_in_months]
    for (var key in goalList) {
      if (goalList.hasOwnProperty(key)) {

        // console.log(key + " - > " + goalList[key])
        var split = goalList[key].split(' ')
        var specificDay = split[1].replace(/,\s*$/, "")  // Regular expression. Remove , and whitespace at end
        // console.log(typeof(specificDay))
        // console.log(typeof(checkedDays[1]))
        // console.log(checkedDays)
        if (checkedDays.includes(parseInt(specificDay))) {
          console.log('Yes')
        }
      }
    }
  }  // renderCalendar function ends here #######################


  var prevChoice = document.querySelector('.prev')
  prevChoice.addEventListener('click', () => {
    date.setMonth(date.getMonth() - 1)
    renderCalendar()
  })

  var prevChoice = document.querySelector('.next')
  prevChoice.addEventListener('click', () => {
    date.setMonth(date.getMonth() + 1)
    renderCalendar()

    // months[month_number_in_months]
})

renderCalendar()
