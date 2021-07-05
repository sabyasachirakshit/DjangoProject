
var myapp={};

// This function is for timer.
function startTimer(duration, display) {
    var timer = duration, minutes, seconds;
    interval=setInterval(function () {
                    minutes = parseInt(timer / 60, 10);
                    seconds = parseInt(timer % 60, 10);
                    hours = "00"
                    minutes = minutes < 10 ? "0" + minutes : minutes;
                    seconds = seconds < 10 ? "0" + seconds : seconds;

                    display.textContent = hours + " : " + minutes + " : " + seconds;
                    stopwatch1=hours + ":" + minutes + ":" + seconds;

                    if (--timer < 0) {
                        timer = duration;
                    }
                    if (stopwatch1 == "00:00:00") {
                        // stop timer
                        clearInterval(interval);
                        // click
                        document.getElementById('submitbtnn').click();            
                    }  
                }, 1000);
 

}

window.onload = function () {
    var fiveMinutes = 299;
        display = document.querySelector('#time');
    startTimer(fiveMinutes, display);
};


/* This function is for correct optons buttons.*/
myapp.count=0;
function click3(n){
   
    var myBtnId=document.getElementById(n);
    var myBtnVl=document.getElementById(n).value;
    
    var myVar = document.getElementById("myVar").value;

    var btnval1=document.getElementById("outlined1").value;
    var btnval2=document.getElementById("outlined2").value;
    var btnval3=document.getElementById("outlined3").value;
    var btnval4=document.getElementById("outlined4").value;

    if(btnval1===myVar)
    { 
        myapp.ansid="outlined1";
    }
    else if(btnval2===myVar)
    {
        myapp.ansid="outlined2";
    }
    else if(btnval3===myVar)
    {
        myapp.ansid="outlined3";
    }
    else if(btnval4===myVar)
    {
        myapp.ansid="outlined4";
    }
    
    if(myBtnId.id==="outlined1"){
        if(myBtnVl===myVar)
        {
             myapp.tempvar=myBtnId.id;
        } 
        else
        {
            myapp.tempvar2=myBtnId.id;
        } 
           
    }
    else if(myBtnId.id==="outlined2"){
        if(myBtnVl===myVar)
        {
             myapp.tempvar=myBtnId.id;
        }
        else
        {
            myapp.tempvar2=myBtnId.id;
        }   
           
    }

    else if(myBtnId.id==="outlined3"){
        if(myBtnVl===myVar)
        {
             myapp.tempvar=myBtnId.id;
        } 
        else
        {
            myapp.tempvar2=myBtnId.id;
        }  
           
    }
    else {
        if(myBtnVl===myVar)
        {
             myapp.tempvar=myBtnId.id;
        } 
        else
        {
            myapp.tempvar2=myBtnId.id;
        }  
           
    }
   
   
}


/*This function is for submit button option.*/

function click2(){
   temp=myapp.tempvar;
   temp2=myapp.tempvar2;
   answerid=myapp.ansid;
   if(temp===answerid)
   {

    document.getElementById(temp).style.backgroundColor="rgb(12, 177, 12)"  

   
   }
   else
   {
    document.getElementById(temp2).style.backgroundColor="red" 
    document.getElementById(answerid).style.backgroundColor="rgb(12, 177, 12)" 

    
   }
}







