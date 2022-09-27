document.getElementById('id').onclick=()=>{
  document.getElementById('id_voted').classList.add('hidden')
}
const prolific_id=document.getElementById("prolific_id_btn")

  prolific_id.addEventListener('click',function(e){
    e.preventDefault()
    
    
    document.getElementById('id_voted').classList.add('hidden')
    const id=document.getElementById('id').value;

    fetch(`/user/${id}`).then(
        response=> response.json()).then(data=> {
        
        
        if (data==='Gen not found'){
            document.getElementById('survey_inactive').classList.remove('hidden')
          }
      else if(data==='Gen found'){
      document.getElementById('intro_page').classList.toggle('hidden')
      document.getElementById('testSection').classList.toggle('hidden') 
      document.getElementById('header_img').classList.add('hidden')

    }
    else if(data==='user voted'){
  
      document.getElementById('id_voted').classList.remove('hidden')
    }
    
        

           
    })
})


document.getElementById('prolific_id_page').addEventListener('click',()=>{
    document.getElementById('intro_page').classList.toggle('hidden')
    document.getElementById('survey_inactive').classList.add('hidden')
    document.getElementById('header_img').classList.remove('hidden')
    document.getElementById('testSection').classList.toggle('hidden')
})

document.getElementById('backToTest').addEventListener('click',()=>{
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

