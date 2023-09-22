const {FlightService} = require("../services");
const axiosInstance = require("../axios")

module.exports = (app) => {

    const flightService = new FlightService();
    
    app.get('/flights', async(req, res) => {
        try
        {
            const flights = await flightService.getFlights()
            res.send({flights:flights})

        }catch(error){
            console.log(error.message);
            res.status(500).send({message:"Sorry we have some problems with the sever.please try later"})
        }
     });

     app.get('/externals', async(req, res) => {
        try
        {
            const flights = await flightService.getExternalFlights()
            res.send({flights:flights})

        }catch(error){
            console.log(error.message);
            res.status(500).send({message:"Sorry we have some problems with the sever.please try later"})
        }
     });
    
     app.get("/external/airports", async(req, res) => {
        try{
            const airports = await flightService.getAirpots();
            res.send(airports);
        }catch(error){
            res.status(500).send({message:"Sorry we have some problems with the sever.please try later"})
        }
     })


}