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
function populate(){
    var route = document.getElementById("selectjourneyRoute");
    var pickup = document.getElementById("selectpickUp");
    var drop = document.getElementById("selectdropping");
    pickup.innerHTML="<option selected disabled value =''>Select an option</option>"
    drop.innerHTML="<option selected disabled value=''>Select an option</option>"
   
  
  
   if(route.value == "MTP6am")
    {
      var pickupArray = ['M1|Boriwali National Park(E)',
                          'M2|Tata Power(Magathane Signal)',
                          'M3|B.H.A.D Colony(Mahindra Gate)',
                          'M4|Samtanagar Police Station stop',
                          'M5|Kurar village(Pushpa Park)',
                          'M6|Oberoi Mall Signal(Labour Room Goregaon)',
                          'M7|Nirlok knowledge Park Goregaon(E)',
                          'M8|Jogeshwari Signal(JVLR Signal)',
                          'M9|Hanuman road bus stand',
                          'M10|Chhatrapati Shivaji Maharaj Smarak',
                          'M11|Vakola signal',
                          'M12|Trade center(BKC Junction)',
                          'M13|Nehru Nagar Tilak Nagar Junction(Kurla)',
                          'M14|Jijamata Bhonsle Marg Junction(Cheddanagar)'
                           ];
      var droppingArray = ['P1|Government Circuit House(Pune)',
                            'P2|Shimla Office',
                            'P3|Pune Central mall',
                            'P4|Ganatra Hotels Pvt Ltd',
                            'P5|Aundh Police Station',
                            'P6|Kaspate Chawk',
                            'P7|Orchid Hotel',
                            'P8|Bhujbal Chawk',
                            'P9|Bhumkar Chawk',
                            'P10|Mukai Chawk'
                            ];
    }
    if(route.value == "PTM1pm")
    {
      var droppingArray = ['M1|Boriwali National Park(E)',
                          'M2|Tata Power(Magathane Signal)',
                          'M3|B.H.A.D Colony(Mahindra Gate)',
                          'M4|Samtanagar Police Station stop',
                          'M5|Kurar village(Pushpa Park)',
                          'M6|Oberoi Mall Signal(Labour Room Goregaon)',
                          'M7|Nirlok knowledge Park Goregaon(E)',
                          'M8|Jogeshwari Signal(JVLR Signal)',
                          'M9|Hanuman road bus stand',
                          'M10|Chhatrapati Shivaji Maharaj Smarak',
                          'M11|Vakola signal',
                          'M12|Trade center(BKC Junction)',
                          'M13|Nehru Nagar Tilak Nagar Junction(Kurla)',
                          'M14|Jijamata Bhonsle Marg Junction(Cheddanagar)'
                           ];
      var pickupArray = ['P1|Government Circuit House(Pune)',
                            'P2|Shimla Office',
                            'P3|Pune Central mall',
                            'P4|Ganatra Hotels Pvt Ltd',
                            'P5|Aundh Police Station',
                            'P6|Kaspate Chawk',
                            'P7|Orchid Hotel',
                            'P8|Bhujbal Chawk',
                            'P9|Bhumkar Chawk',
                            'P10|Mukai Chawk'
                            ];
    }
    for(var option in pickupArray)
    {
       var pair = pickupArray[option].split("|");
       var newoption = document.createElement("option");
  
       newoption.value = pair[0];
       newoption.innerHTML = pair[1];
       pickup.options.add(newoption);
    }
    for(var option in droppingArray)
    {
       var pair = droppingArray[option].split("|");
       var newoption = document.createElement("option");
  
       newoption.value = pair[0];
       newoption.innerHTML = pair[1];
       drop.options.add(newoption);
    }
}




/*function localstorage(){
  var datefield = document.getElementById("selectdateOfJourney");
  var route = document.getElementById("selectjourneyRoute");
  var name = document.getElementById("nameOfCustomer");
  var mobileno = document.getElementById("mobileNoOfCustomer");
  var seatnumber = document.getElementById("selectseatNumber");
  var pickup = document.getElementById("selectpickUp");
  var drop = document.getElementById("selectdropping");
  var luggage = document.getElementById("luggageDetails");

  localStorage.setItem('datefield',datefield.value);
  localStorage.setItem('route',route.value);
  localStorage.setItem('name',name.value);
  localStorage.setItem('mobileno',mobileno.value);
  localStorage.setItem('seatnumber',seatnumber.value);
  localStorage.setItem('pickup',pickup.value);
  localStorage.setItem('drop',drop.value);
  localStorage.setItem('luggage',luggage.value);

}*/

function availableseats(){
  date = document.getElementById("selectdateOfJourney").value;
  route = document.getElementById("selectjourneyRoute").value;
  if(date==null||route==null){
    return "20221004";
  }
  else{
    strdate = date.toString()
    k = strdate.replace('-',"")+route.slice(0,3);
    return k;

  }
  
}
