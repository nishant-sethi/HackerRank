  
var clickbtn= document.getElementById('btn');
    var count=0;
  clickbtn.onclick=function(){
      count+=1;
      clickbtn.innerHTML=count;
  } 