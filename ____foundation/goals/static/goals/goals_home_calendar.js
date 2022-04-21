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

  let daysDict = {}
  let checkedDays = []
  const monthDays = document.querySelector('.days')
  for(let i = 1; i<= lastDayDate; i++) {
      daysDict[i] += `<div class="day-block">`
      daysDict[i] = daysDict[i].replace('undefined', '')
    if(i === new Date().getDate() && date.getMonth() === new Date().getMonth()){
      // days += `<div class="today">${i}</div>`;
      daysDict[i] += `<div class="today">${i}</div>`;
      daysDict[i] = daysDict[i].replace('undefined', '')
      checkedDays.push(i)
    } else {
      // days += `<div class="day${i}">${i}</div>`
      checkedDays.push(i)
      for (var key in goalList) {
        if (goalList.hasOwnProperty(key)) {

          // console.log(key + " - > " + goalList[key])
          var specificDate = goalList[key].split(' ')
          var specificYear = specificDate[2]
          var specificMonth = specificDate[0]
          var specificDay = specificDate[1].replace(/,\s*$/, "")  // Regular expression. Remove , and whitespace at end
          var specificEvent = key
          if (i === parseInt(specificDay) &&
          date.getFullYear() === parseInt(specificYear) &&
          months[date.getMonth()] === specificMonth) {
            // days += `<div class="day${i} event_${specificEvent}">Deadline</div>`
            daysDict[i] += `<div class="day${i} event">${specificEvent}</div>`
            daysDict[i] = daysDict[i].replace('undefined', '')
            checkedDays.push(i)
          }
        }
      }
      // days += `<div class="day${i}">${i}</div>`
      if (i in daysDict) {
      daysDict[i] += `<div class="day${i}">${i}</div>`
      daysDict[i] = daysDict[i].replace('undefined', '')
      } else {
        daysDict[i] += `<div class="day${i}">${i}</div>`
        daysDict[i] = daysDict[i].replace('undefined', '')
      }
    }
    daysDict[i] += `</div>`
    daysDict[i] = daysDict[i].replace('undefined', '')
  }

  for(let j=1; j<=nextDays; j++) {
    days += `<div class="next-date">${j}</div>`
  }
    // console.log(monthDays)
    // console.log(days)
    // console.log(daysDict)
    for (var key in daysDict) {
      // console.log(daysDict[key])
      days += daysDict[key]
    }
    monthDays.innerHTML = days;

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

console.log(goalList)
