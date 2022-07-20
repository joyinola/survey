const prolific_id=document.getElementsByClassName("prolific_id")
for(const i of prolific_id){
i.addEventListener('submit',function(e){
    e.preventDefault()
    
    console.log('next clicked')
    document.getElementById('id_voted').classList.add('hidden')
    const id=document.getElementById('id').value;

    fetch(`/user/${id}`).then(
        response=> response.json()).then(data=> {
          // console.log(data)
        
        if (data==='Gen not found'){
            document.getElementById('survey_inactive').classList.remove('hidden')
          }
      else if(data==='Gen found'){
      document.getElementById('intro').classList.toggle('hidden')
      document.getElementById('Instructions').classList.toggle('hidden') 

    }
    else if(data==='user voted'){
  
      document.getElementById('id_voted').classList.remove('hidden')
    }
    
        

           
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
document.getElementById('backToTest').addEventListener('click',()=>{
  document.getElementById('Instructions').classList.add('hidden')
  document.getElementById('headlines1').classList.add('hidden')

  document.getElementById('testSection').classList.remove('hidden')
})
function puce(e){
  e.preventDefault()
  const testInput=document.getElementById('testInput').value

if(testInput==''){
   document.getElementById('inputerror').classList.remove('hidden')
}
else{

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
    if (data==='session expired'){
                               
      document.getElementById('expired_session').classList.remove('hidden')
      
      window.onbeforeunload= ()=>{
        window.setTimeout(()=>{
            window.location='/'
        },0)
        window.onbeforeunload=null
      }
    }
    else{
   document.getElementById('inputerror').classList.add('hidden')
   document.getElementById('Instructions').classList.add('hidden')
    document.getElementById('testSection').classList.toggle('hidden')
    document.getElementById('headlines1').classList.toggle('hidden')}
  })

  }
  
}

const test=document.getElementsByClassName('test')
for (const i of test){
  i.addEventListener('click', (e)=>{puce(e)})

  
}
// document.getElementById('puceform').addEventListener('submit',(e)=>{
//   e.preventDefault()
//   puce(e)})
document.getElementById('headlines2').addEventListener('click',()=>{
   

    window.location.href="/headlines/1"
  })

