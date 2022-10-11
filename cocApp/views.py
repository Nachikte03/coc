from django.contrib import messages
from django.shortcuts import render
from .models import CabBooking


def homepage(request):
    return render(request,'homepage.html')

def checkbooking(request):
    return render(request,'checkbooking.html')


def bookingform(request):
    if request.method=='POST':
          txtDate = request.POST.get('selectdateOfJourney')
          txtCabRouteValue = request.POST.get('selectjourneyRoute')
          print(txtCabRouteValue)
          tocheckseat = str(str(txtDate).replace("-","")+"/"+txtCabRouteValue[0:3])
          if txtCabRouteValue[0:3]== "MTP":
            Route = "Mumbao to Pune - (6 A.M.)"
            pickuparray = {'M1':['National Park,Boriwali(E)-6:00 am','6:00 AM'],
                 'M2':['Tata Power(Magathane Signal)-6:02 am','6:00 AM'],
                 'M3':['Samtanagar/Bandongari bus stop-6:05 am','6:00 AM'],
                 'M4':[' Pushpapark/ Kurar village-6:05 am','6:00 AM'],
                  'M5':['Oberoi Mall Signal-6:10 am','6:00 AM'],
                  'M6':['Hanuman road bus stand-6:20 am','6:00 AM'],
                  'M7':['Chhatrapati Shivaji Maharaj Smarak-6:20 am','6:00 AM'],
                  'M8':['Vakola signa-6:30 am','6:00 AM'],
                  'M9':['BKC junction/Trade center-6:40 am','6:00 AM'],
                  'M10':['Kurla-6:40 am','6:00 AM'],
                  'M11':['Cheddanagar-6:45 am','6:00 AM'],}
            droppingarray = {
                  'P1':['Government Circuit House ','6:00 AM'],
                  'P2':['Shimla Office ','6:00 AM'],
                  'P3':['Pune Central mall ','6:00 AM'],
                  'P4':['Ganatra Hotels Pvt Ltd ','6:00 AM'],
                  'P5':['Aundh Police Station ','6:00 AM'],
                  'P6':['Kaspate Chawk ','6:00 AM'],
                  'P7':['Orchid Hotel ','6:00 AM'],
                  'P8':['Bhujbal Chawk ','6:00 AM'],
                  'P9':['Bhumkar Chawk ','6:00 AM'],
                  'P10':['Mukai Chawk ','6:00 AM']
                  }
          else:
            Route = "Pune to Mumbai - 1 P.M."
            droppingarray = {'M1':['National Park,Boriwali(E)-6:00 am','6:00 AM'],
                 'M2':['Tata Power(Magathane Signal)-6:02 am','6:00 AM'],
                 'M3':['Samtanagar/Bandongari bus stop-6:05 am','6:00 AM'],
                 'M4':[' Pushpapark/ Kurar village-6:05 am','6:00 AM'],
                  'M5':['Oberoi Mall Signal-6:10 am','6:00 AM'],
                  'M6':['Hanuman road bus stand-6:20 am','6:00 AM'],
                  'M7':['Chhatrapati Shivaji Maharaj Smarak-6:20 am','6:00 AM'],
                  'M8':['Vakola signa-6:30 am','6:00 AM'],
                  'M9':['BKC junction/Trade center-6:40 am','6:00 AM'],
                  'M10':['Kurla-6:40 am','6:00 AM'],
                  'M11':['Cheddanagar-6:45 am','6:00 AM'],}
            pickuparray = {
                  'P1':['Government Circuit House ','6:00 AM'],
                  'P2':['Shimla Office ','6:00 AM'],
                  'P3':['Pune Central mall ','6:00 AM'],
                  'P4':['Ganatra Hotels Pvt Ltd ','6:00 AM'],
                  'P5':['Aundh Police Station ','6:00 AM'],
                  'P6':['Kaspate Chawk ','6:00 AM'],
                  'P7':['Orchid Hotel ','6:00 AM'],
                  'P8':['Bhujbal Chawk ','6:00 AM'],
                  'P9':['Bhumkar Chawk ','6:00 AM'],
                  'P10':['Mukai Chawk ','6:00 AM']
                  }
          bookingid_iterator = CabBooking.objects.values_list('bookingid').iterator()
          bookingid_list = [i for i in bookingid_iterator]
          data = [x for (x,) in bookingid_list]
          dateroute = [x.replace("-"," ").split(" ")[0] for x in data]
          seat = [x.replace("-"," ").split(" ")[1] for x in data]
          tuplelist = [(dateroute[i], seat[i]) for i in range(0, len(dateroute))]
          daterouteseat = {}
          for (key, value) in tuplelist:
             if key in daterouteseat:
              daterouteseat[key].append(value)
             else:
              daterouteseat[key] = [value]
          
          if tocheckseat in daterouteseat:
            return render(request,'bookingform.html',{'pickuparray':pickuparray,
          'droppingarray':droppingarray,'data':daterouteseat,'n':['1','2','3','4','5'],'txtDate':txtDate,'txtCabRouteValue':txtCabRouteValue,'Route':Route,'tocheckseat':tocheckseat})
          else:
            return render(request,'bookingform.html',{'key':True,'pickuparray':pickuparray,
          'droppingarray':droppingarray,'data':daterouteseat,'n':['1','2','3','4','5'],'txtDate':txtDate,'txtCabRouteValue':txtCabRouteValue,'Route':Route,'tocheckseat':tocheckseat})
          
          
    else:
         return render(request,'checkbooking.html')






def confirm(request):
    if request.method == 'POST':
        txtName = request.POST.get('nameOfCustomer')
        txtContactNumber = request.POST.get('mobileNoOfCustomer')
        txtDate = request.POST.get('selectdateOfJourney')
        print(txtDate)
        txtCabRouteValue = request.POST.get('selectjourneyRoute')
        txtRouteOfJourney = request.POST.get('selectjourneyRoute')
        txtSeatNumberValue = request.POST.get('selectseatNumber')
        txtCabDetails = "Grey Ertiga (1759)"
        txtPickUpLocationValue = request.POST.get('selectpickUp')
        DroppingLocationValue = request.POST.get('selectdropping')
        txtLuggage = request.POST.get('luggaeDetails')

        Locations = {'M1':['National Park,Boriwali(E)-6:00 am','6:00 AM'],
                 'M2':['Tata Power(Magathane Signal)-6:02 am','6:00 AM'],
                 'M3':['Samtanagar/Bandongari bus stop-6:05 am','6:00 AM'],
                 'M4':[' Pushpapark/ Kurar village-6:05 am','6:00 AM'],
                  'M5':['Oberoi Mall Signal-6:10 am','6:00 AM'],
                  'M6':['Hanuman road bus stand-6:20 am','6:00 AM'],
                  'M7':['Chhatrapati Shivaji Maharaj Smarak-6:20 am','6:00 AM'],
                  'M8':['Vakola signa-6:30 am','6:00 AM'],
                  'M9':['BKC junction/Trade center-6:40 am','6:00 AM'],
                  'M10':['Kurla-6:40 am','6:00 AM'],
                  'M11':['Cheddanagar-6:45 am','6:00 AM'],
                  'P1':['Government Circuit House ','6:00 AM'],
                  'P2':['Shimla Office ','6:00 AM'],
                  'P3':['Pune Central mall ','6:00 AM'],
                  'P4':['Ganatra Hotels Pvt Ltd ','6:00 AM'],
                  'P5':['Aundh Police Station ','6:00 AM'],
                  'P6':['Kaspate Chawk ','6:00 AM'],
                  'P7':['Orchid Hotel ','6:00 AM'],
                  'P8':['Bhujbal Chawk ','6:00 AM'],
                  'P9':['Bhumkar Chawk ','6:00 AM'],
                  'P10':['Mukai Chawk ','6:00 AM']
                  };

        txtPickUpLocation = Locations[txtPickUpLocationValue][0]
        DroppingLocation = Locations[DroppingLocationValue][0]
        txtPickUpTime = Locations[txtPickUpLocationValue][1]
        amountArray = {'1':'500','2':'450','3':'450','4':'400','5':'400'}
        txtBookingAmount = amountArray[txtSeatNumberValue]
        bookingid1 = str(txtDate).replace("-","")+"/"+txtCabRouteValue[0:3]+"-"+txtSeatNumberValue
        strdate = str(txtDate).replace("-","")
        TicketNumber = strdate+txtCabRouteValue[0:3]+txtSeatNumberValue+txtName[0:3].upper()+txtContactNumber[-4:]
        
        
        
        
        #Working on DataBase
        bookings = CabBooking.objects.all()
        if bookings.filter(bookingid=bookingid1):
            CRITICAL = 50
            messages.add_message(request, CRITICAL, 'A very serious error ocurred.')
            return render(request, 'bookingform.html',{'m':'m'})
        else:
            instant = CabBooking(
                 bookingid = bookingid1,
                 ticketNo = TicketNumber,
                 journeyDate = txtDate,
                 routeValue = txtCabRouteValue,
                 route = txtRouteOfJourney,
                 name = txtName,
                 mobileNo = txtContactNumber,
                 seatNo = txtSeatNumberValue,
                 pickupTime = txtPickUpTime,
                 pickupValue = txtPickUpLocationValue,
                 pickupLocation = txtPickUpLocation,
                 droppingLocation = DroppingLocation,
                 droppingValue = DroppingLocationValue,
                 luggage = txtLuggage,
                 amount = txtBookingAmount,)
            instant.save()
        
        data={
            'txtDateOfJourney':txtDate,
            'txtSeatNumber':txtSeatNumberValue,
            'txtCabDetails':txtCabDetails,
            'txtPickUpTime':txtPickUpTime,  
            'txtPickUpLocationValue':txtPickUpLocationValue,
            'txtPickUpLocation':txtPickUpLocation,
            'txtLuggage':txtLuggage,
            'txtBookingAmount':txtBookingAmount,
            'TicketNumber':TicketNumber,
            'bookings':bookings,
        }
    
        return render(request, 'confirm.html',data)
    else:
        return render(request, 'confirm.html')




def payment(request):
    return render(request,'payment.html')
def terms(request):
    return render(request,'payment.html')
def cancelbooking(request):
    return render(request,'payment.html')
def changeseat(request):
    return render(request,'payment.html')
def livelocation(request):
    return render(request,'payment.html')
