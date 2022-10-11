 



function datefield(){
    const today = new Date();
    const maxdate = new Date();
    const mindate = new Date();
    
    maxdate.setDate(today.getDate()+30);
    
    var mndate = mindate.toISOString().slice(0,10);
    var mxdate = maxdate.toISOString().slice(0,10);
    
    var datefield = document.getElementById("selectdateOfJourney");
    datefield.setAttribute("max",mxdate);
    datefield.setAttribute("min",mndate);
    }
      
    
      
    
    
    
    
     
       
    
     
    
    