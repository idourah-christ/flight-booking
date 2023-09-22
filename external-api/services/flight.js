const axiosInstance = require("../axios");


class FlightService{

    async getFlights(){
        try{
            const response = await axiosInstance.get("/");
            return response.data;

        }catch(error){
            console.log(error);
            throw Error("GetAllBookingException error: " + error);
        }     
    }

    async getExternalFlights(){
        try{
            
            return [{'data':"external flights"}];

        }catch(error){
            console.log(error);
            throw Error("GetAllBookingException error: " + error);
        }     
    }
    async getAirpots(){
        try{
            const response = await axiosInstance.get("https://3ddc-185-235-207-212.ngrok-free.app/airports");
            return response.data;

        }catch(error){
            throw Error(error.message);
        }
    }
}

module.exports = FlightService;