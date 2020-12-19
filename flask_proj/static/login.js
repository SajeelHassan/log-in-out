
var l_uname=document.getElementById('login-username');
var l_pwd=document.getElementById('login-password');
var l_submit=document.getElementById('login-btn');
if(l_submit)
    l_submit.addEventListener('click',onLogin);

function onLogin(event){
    if(notEmpty()!=true){
        let msgBlock=document.getElementById('message-block');
        msgBlock.style.display='inline-block';
        let msgP=document.getElementById('l_empty');
        msgP.style.display='block';
        setTimeout(function(){
            msgP.style.display='none';
            msgBlock.style.display='none';
        },3000);
    }
    else{
        let pwd=l_pwd.value;
        let token='';
        for (let i=0;i<pwd.length;i++){
            token+=pwd.charCodeAt(i);
        }
        var data={
                "username":`${l_uname.value}`,
                "password":`${token}`
        }
        token=""
        var jsonString=JSON.stringify(data);
        var xmlObj=new XMLHttpRequest();
        xmlObj.open('post','loggingin',true);
        xmlObj.onload=function(){
            if(this.status===200){
                    if(this.responseText!='VALID')
                    {
                        l_uname.value='';
                        l_pwd.value='';
                        let msgBlock=document.getElementById('message-block');
                        msgBlock.style.display='inline-block';
                        let msgP=document.getElementById('i_uname-pwd');
                        msgP.style.display='block';
                        setTimeout(function(){
                            msgP.style.display='none';
                            msgBlock.style.display='none';
                        },3000);
                    }
                    else
                        {
                            window.location.href = "dashboard";
                        }
            }
        }
        xmlObj.setRequestHeader("content-Type","application/json");
        token=""
        xmlObj.send(jsonString);
    }
    event.preventDefault();
}
function notEmpty(){
    if(l_pwd.value=='' ||l_uname.value=='')
        return false;
    return true;
}