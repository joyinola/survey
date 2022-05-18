window.onload= ()=>{

const genInfo=document.getElementsByClassName('genInfo')
for (i of genInfo){
    i.addEventListener('click',()=>{

        document.getElementById('politics').classList.toggle('hidden')
        document.getElementById('info').classList.toggle('hidden')
        document.getElementById('selectItem').classList.add('hidden')}
        )
}

const submit=document.getElementById('submitInfo')
if (submit){
submit.addEventListener('click', (e)=>{
    e.preventDefault()
const radio=document.querySelector('input[type=radio][name=Gender]:checked')

    if (radio){
        radioValue=radio.value
    }
    else{
        radioValue=''
    }

const userInfo={
"gender":radioValue,
"age":document.getElementById('age').value,
"qualifications":document.getElementById('qualification').value,
"interest":document.getElementById('interest').value,
"candidate":document.getElementById('candidate').value,
"republican":document.getElementById('republican').value,
    }

    if (userInfo["gender"]===''||userInfo["age"]===''||userInfo["qualifications"]===''||userInfo["interest"]===''||userInfo["candidate"]===''||userInfo["republican"]===''){
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
    document.getElementById('info').classList.add('hidden');
    document.getElementById('politics').classList.add('hidden')
    document.getElementById('confirmcode').innerHTML=`Your survey has been submitted 
    successfully below is your confirmation code ${data}`;
    document.getElementById('selectItem').classList.add('hidden')
    document.getElementById('code').classList.remove('hidden');
    
})}})}}