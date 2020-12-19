
var s_fname=document.getElementById('fullname');
var s_email=document.getElementById('email');
var s_uname=document.getElementById('signup-username');
var s_pwd=document.getElementById('signup-password');
var s_pwd_cf=document.getElementById('signup-password-confirm');
var s_submit=document.getElementById('signup-btn')
s_submit.addEventListener('click',goForSignup);
var token="";
function goForSignup(e){
    if(isvalid()!=true){
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
        if(s_pwd.value!=s_pwd_cf.value){
            let msgBlock=document.getElementById('message-block');
            let msgP=document.getElementById('i_uname-pwd');
            msgP.style.display='block';
            msgP.innerText='Those passwords didn\'t match. Try again';
            msgBlock.style.display='inline-block';
            setTimeout(function(){
                msgP.style.display='none';
                msgBlock.style.display='none';
                },3000);
        }
        else{
            let pwd=s_pwd.value;
            for (let i=0;i<pwd.length;i++){
                token+=pwd.charCodeAt(i);
            }
            var data={
                "fullname":`${s_fname.value}`,
                "email":`${s_email.value}`,
                "username":`${s_uname.value}`,
                "password":`${token}`
            }
            token=""
            var jsonString=JSON.stringify(data);
            var xmlObj=new XMLHttpRequest();
            xmlObj.open('post','signup',true);
            xmlObj.onload=function(){
                if(this.status===200){
                    if(this.responseText!='VALID'){
                        let msgBlock=document.getElementById('message-block');
                        let msgP=document.getElementById('i_uname-pwd');
                        msgP.style.display='block';
                        msgP.innerText=this.responseText;
                        msgBlock.style.display='inline-block';
                        setTimeout(function(){
                            msgP.style.display='none';
                            msgBlock.style.display='none';
                        },3000);

                    }
                     else{
                    window.location.href = "dashboard";
                     }
                    }
                }
                xmlObj.setRequestHeader("content-Type","application/json");
                token=""
                xmlObj.send(jsonString);
            }



        }

    e.preventDefault();
}
function isvalid(){
    if(s_fname.value =="" || s_email.value=='' || s_uname.value=='' || s_pwd.value=='' ||s_pwd_cf.value==''){
        return false
    }
    return true
}