const counters = document.querySelectorAll('.counter')
let count = 1
counters.forEach((div)=>{
    div.innerText=count
    count+=1
})