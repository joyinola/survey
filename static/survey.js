const prolific_id=document.getElementsByClassName("prolific_id")
for(const i of prolific_id){
i.addEventListener('submit',function(e){
    e.preventDefault()
    
    console.log('next clicked')
    const id=document.getElementById('id').value;

    fetch(`/user/${id}`).then(
        response=> response.json()).then(data=> 
        {
          if (data==='Gen not found'){
            document.getElementById('survey_inactive').classList.remove('hidden')
          }
          else{
      document.getElementById('intro').classList.toggle('hidden')
      document.getElementById('Instructions').classList.toggle('hidden') 

    }
     // document.getElementById('testSection').classList.toggle('hidden')
        

           
    }).catch(err=>console.log(err))
})}


document.getElementById('prolific_id_page').addEventListener('click',()=>{
    document.getElementById('intro').classList.toggle('hidden')
    document.getElementById('survey_inactive').classList.add('hidden')
    document.getElementById('Instructions').classList.toggle('hidden')
})
const goToTest=document.getElementsByClassName("goToTest")
for(i of goToTest){
  i.addEventListener('click',()=>{
    document.getElementById('Instructions').classList.toggle('hidden')
    document.getElementById('testSection').classList.toggle('hidden')
  })
}
// const dummy=document.getElementsByClassName('dummy')
// for (i of dummy){
//   i.addEventListener('click',()=>{
//     document.getElementById('Instructions').classList.toggle('hidden')
//      document.getElementById('dummy').classList.toggle('hidden')
//   })
// }
const test=document.getElementsByClassName('test')
for (const i of test){
  i.addEventListener('click', function(e){
    const testInput=document.getElementById('testInput').value
    e.preventDefault()
    console.log('continue clicked')
  if(testInput==''){
     document.getElementById('inputerror').classList.remove('hidden')
  }
  else{
    // console.log('success')
    fetch('/test/',
      {
      method:'POST',
      headers:
      {
        'Content-Type':'application/json'
      },
      body:JSON.stringify({'testInput':testInput})
    }
      ).then(response=>response.json()).then(data=>{
      console.log(data)
     document.getElementById('inputerror').classList.add('hidden')
      document.getElementById('testSection').classList.toggle('hidden')
      document.getElementById('headlines1').classList.toggle('hidden')})

    }
      
     
    
  }
  ) }
  document.getElementById('headlines2').addEventListener('click',()=>{
   

    window.location.href="/headlines/1"
  })

