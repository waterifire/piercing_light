// console.log(goalList)



const editBtns = document.querySelectorAll(".edit")
const cancelBtns = document.querySelectorAll(".btnCancel")
// console.log(editBtns)

// Edit ######################################################################

// Adding event listeners to each edit button
let i = 0
editBtns.forEach(edit => {
  edit.addEventListener("click", editMe)

  edit.setAttribute('id', `btn_${goalList[i]}`.toLowerCase())
  i ++
})

// showing and hidding correct boxes
function editMe(clicked_id) {
  // console.log(event.srcElement.id)
  let srcGoal = event.srcElement.id.replace(RegExp(/^btn_/), '')
  // console.log(srcGoal)

  let focusGoal = document.getElementById(`goal--${srcGoal}`)
  let focusForm = document.getElementById(`form--${srcGoal}`)
  focusGoal.classList.add("hide_me")
  focusForm.classList.remove("form_hide")
  focusForm.classList.add("show_me")



  // console.log(usedStr)
  //
  // let locStr = document.getElementById('id_name')
  // locStr.placeholder = usedStr
}


//placeholder
let locaStrs = document.querySelectorAll('.goal-edit')
a = 0
locaStrs.forEach(loca => {
  let srcGoal = goalList[a]
  // console.log(srcStr.textContent)
  loca.placeholder = srcGoal
  a ++
})


// Cancel button
let j = 0
cancelBtns.forEach(cancel => {
  cancel.addEventListener("click", cancelNow)
  cancel.setAttribute('id', `cancel--${goalList[j]}`.toLowerCase())
  j ++
})

function cancelNow(clicked_id) {
  // console.log(event.srcElement.id)
  let srcGoal = event.srcElement.id.replace(RegExp(/^cancel--/), '')
  // console.log(srcGoal)

  let focusGoal = document.getElementById(`goal--${srcGoal}`)
  let focusForm = document.getElementById(`form--${srcGoal}`)
  focusGoal.classList.remove("hide_me")
  focusForm.classList.add("form_hide")
  focusForm.classList.remove("show_me")
}

// remove ###############################################################
