window.onload= ()=>{

document.getElementById('backToGen').addEventListener('click',()=>{
    document.getElementById('politics').classList.toggle('hidden')
    document.getElementById('info').classList.toggle('hidden')
    document.getElementById('selectItem').classList.add('hidden')
})
const genInfo=document.getElementById('genInfo')

    genInfo.addEventListener('click',()=>{

    
    const radio=document.querySelector('input[type=radio][name=Gender]:checked')

    if (radio){
        radioValue=radio.value
    }
    else{
        radioValue=''
    }
        const userInfo1={
            "gender":radioValue,
            "age":document.getElementById('age').value,
            "qualifications":document.getElementById('qualification').value,
            // "first":true
            }
            
           
            if (userInfo1["gender"]===''||userInfo1["age"]===''||userInfo1["qualifications"]===''){
                document.getElementById('error').innerHTML='FILL OUT ALL FORMS BEFORE PROCEEDING!'
                document.getElementById('selectItem').classList.remove('hidden')
            }
          
            else if (isNaN(userInfo1['age']) || !Number.isInteger(parseFloat(userInfo1['age']))){
                document.getElementById('error').innerHTML='Invalid Age'
                document.getElementById('selectItem').classList.remove('hidden')
            }
            else{

                url='/info/'
                fetch(url,{
                    method:'POST',
                    headers:{
                        'Content-Type':'application/json',
                    },body:JSON.stringify({userInfo1})
            }).then(response=>response.json()).then(data=>{
                console.log(data)
                console.log(userInfo1)
                if (data==='session expired'){
                    document.getElementById('expired_session').classList.remove('hidden')
                    windows.location=''
                  }
                  else{
            document.getElementById('politics').classList.toggle('hidden')
            document.getElementById('info').classList.toggle('hidden')
            document.getElementById('selectItem').classList.add('hidden')}
        })}})

const submit=document.getElementById('submitInfo')
if (submit){
submit.addEventListener('click', (e)=>{
    e.preventDefault()


const userInfo={
"interest":document.getElementById('interest').value,
"candidate":document.getElementById('candidate').value,
"republican":document.getElementById('republican').value,
    }
    

    if (userInfo["interest"]===''||userInfo["candidate"]===''||userInfo["republican"]===''){
        document.getElementById('error').innerHTML='FILL OUT ALL FORMS BEFORE PROCEEDING!'
        document.getElementById('selectItem').classList.remove('hidden')
    }
    
else{
    url='/info/'
    fetch(url,{
        method:'POST',
        headers:{
            'Content-Type':'application/json',
        },body:JSON.stringify({userInfo})
}).then(response=>response.json()).then(data=>{
    console.log(data)
    if (data==='session expired'){
        document.getElementById('expired_session').classList.remove('hidden')
        window.location=''
      }
      else{
    document.getElementById('info').classList.add('hidden');
    document.getElementById('politics').classList.add('hidden')
    document.getElementById('confirmcode').innerHTML=`Your survey has been submitted 
    successfully below is your confirmation code ${data}`;
    document.getElementById('selectItem').classList.add('hidden')
    document.getElementById('code').classList.remove('hidden');}
    
}
)}})}}