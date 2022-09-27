window.onload= ()=>{
   const input= document.getElementsByTagName('input')

   for (i of input){
   i.addEventListener('click',()=>{
    document.getElementById('selectItem').classList.add('hidden')
    document.getElementById('error').classList.add('hidden')
    document.getElementsByClassName('selectItem2')[0].classList.add('hidden')
        }) }

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
                  
                    document.getElementById('selectItem').classList.remove('hidden')
                    document.getElementById('error').classList.add('hidden')
                }
              
                else if (isNaN(userInfo1['age']) || !Number.isInteger(parseFloat(userInfo1['age']))){   
                    document.getElementById('error').classList.remove('hidden')
                    document.getElementById('selectItem').classList.add('hidden')
                }
                else{
                    fetch('/info/',{
                        method:'POST',
                        headers:{
                            'Content-Type':'application/json'
                        },body:JSON.stringify({userInfo1})
                }).then(response=>response.json()).then(data=>{
                    console.log(data)
                    console.log(userInfo1)
                    if (data==='session expired'){
                        document.getElementById('selectItem').classList.add('hidden')
                        document.getElementById('error').classList.add('hidden')
                        document.getElementById('expired_session').classList.remove('hidden')
                        window.onbeforeunload= ()=>{
                            window.setTimeout(()=>{
                                window.location='/'
                            },0)
                            window.onbeforeunload=null
                          }
                      }
                      else{
                document.getElementById('politics').classList.toggle('hidden')
                document.getElementById('info').classList.toggle('hidden')
                document.getElementById('selectItem').classList.add('hidden')
                document.getElementById('error').classList.add('hidden')
            }
            })}})
    
    const submit=document.getElementById('submitInfo')
    if (submit){
    submit.addEventListener('click', (e)=>{
        e.preventDefault()
    
    
    const userInfo={
    "interest":document.getElementById('interest').value,
    "candidate":document.getElementById('candidate').value,
    "republican":document.getElementById('republican').value
        }
    
    
    if (userInfo["interest"]==='' || userInfo["candidate"]==='' || userInfo["republican"]===''){
            
        document.getElementsByClassName('selectItem2')[0].classList.remove('hidden')
        }
    
    else{
        fetch('/info/',{
            method:'POST',
            headers:{
                'Content-Type':'application/json'
            },body:JSON.stringify({userInfo})
    }).then(response=>response.json()).then((data)=>{
        console.log(data)
        if (data==='session expired'){
            document.getElementsByClassName('selectItem2')[0].classList.add('hidden')
            document.getElementById('error').classList.add('hidden')                     
            document.getElementById('expired_session').classList.remove('hidden')
          
            window.onbeforeunload= ()=>{
              window.setTimeout(()=>{
                  window.location='/'
              },0)
              window.onbeforeunload=null
            }
          }
          else if(data==='no data'){
            document.getElementById('info').classList.add('hidden');
            document.getElementById('politics').classList.add('hidden');
            document.getElementById('code').classList.remove('hidden');
            document.getElementById('confirmcode').innerHTML=`Please ensure you partake in the voting excercise`;
            document.getElementsByClassName('selectItem2')[0].classList.add('hidden')  
        }
          else{
        document.getElementById('info').classList.add('hidden');
        document.getElementById('politics').classList.add('hidden');
        document.getElementById('confirmcode').innerHTML=`Your survey has been submitted 
        successfully below is your confirmation code ${data}`;
        document.getElementsByClassName('selectItem2')[0].classList.add('hidden')
        // document.getElementById('error').classList.add('hidden')
    
        document.getElementById('code').classList.remove('hidden');
    
    
        window.onbeforeunload= ()=>{
            window.setTimeout(()=>{
                window.location='/'
            },0)
            window.onbeforeunload=null
          }
        
    
    
        
    }
        
    }
    )}})}}