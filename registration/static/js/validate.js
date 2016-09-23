
function text(inputid){
	var a=document.getElementById(inputid);
	var check=/^[A-Za-z]+$/;
	if(inputid=='fname')
		var idele='error';
	else
		idele='error2';
	if(!check.test(a.value))
	{
		a.value="";
    document.getElementById(idele).innerHTML="Name should contain alphabets";
    }else
  
    document.getElementById(idele).innerHTML="";
}
function usern(inputid)
{   var a=document.getElementById(inputid);
	var check=/^[-\w\.\$@\*\!]{5,30}$/;
	if(!check.test(a.value))
	{
		document.getElementById('usererror').innerHTML="Minimum 5 characters without space";
		a.value="";
	}
	else
		document.getElementById('usererror').innerHTML="";
}
function passn(inputid)
{
	var a=document.getElementById(inputid);
	var check=/^[-\w\@\#\%\^\&\*\']{6,20}$/;
	if(!check.test(a.value))
	{
		document.getElementById('passerror').innerHTML="Minimum 6 character long";
		a.value="";
	}
	else
		document.getElementById('passerror').innerHTML="";

}
function mailn(inputid)
{
	var a=document.getElementById(inputid);
	var check=/^\w{2,30}@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$/;
	if(!check.test(a.value)){
		a,value="";
		document.getElementById('mailerror').innerHTML="Invalid Pattern of email";
	}
	else
		document.getElementById('mailerror').innerHTML="";
}
function confpassn(inputid)
{
	var a=document.getElementById(inputid);
	if(document.getElementById('pass').value!=a.value){
		a.value="";
		document.getElementById('conferror').innerHTML="Password Does Not Match";
	}else
		document.getElementById('conferror').innerHTML="";

}
function phone(inputid)
{
	var a=document.getElementById(inputid);
	var check=/^\d{10}$/;
	if(!check.test(a.value))	
	{	
		a.value="";
       document.getElementById('phoneerror').innerHTML="Fill correct Phone Number";
    }	
     else
		document.getElementById('phoneerror').innerHTML="";

}
