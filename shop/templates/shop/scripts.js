const getLocation = document.getElementById("get location");

getLocation.addEventListener('click',evt=>{
    if('geolocation' in navigator){
        navigator.geolocation.getCurrentPosition(position=>{
            let latitude = position.coords.latitude;
            let longitude = position.coords.longitude;

            let googleMapURL = `https://maps.googleapis.com/maps/api/staticmap?center=${latitude},${longitude}&zoom=11&size=400x400`;
            
            console.log(latitude,longitude)
        },error=>{
            console.log(error.code);
        });
    }else{
        console.log("Not Supported")
    }
});