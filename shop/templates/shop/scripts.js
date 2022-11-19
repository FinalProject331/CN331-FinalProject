const getLocation = document.getElementById("get location");

getLocation.addEventListener('click',evt=>{
    if('geolocation' in navigator){
        navigator.geolocation.getCurrentPosition(position=>{
            let latitude = position.coords.latitude;
            let longitude = position.coords.longitude;

            console.log(latitude)
        },error=>{
            console.log(error.code);
        });
    }else{
        console.log("Not Supported")
    }
});