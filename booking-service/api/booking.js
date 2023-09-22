const {BookingService} = require("../services");
const CancelBooking = require("./cancel-booking");
const axiosInstance = require("../axios")

module.exports = (app) => {

    const bookingService = new BookingService();
    const cancelBooking = new CancelBooking();

    app.get('/', async(req, res) => {
        try
        {
            const bookins = await bookingService.getAllBooking()
            res.send({bookings:bookins})

        }catch(error){
            console.log(error.message);
            res.status(500).send({message:"Sorry we have some problems with the sever.please try later"})
        }
     });
     app.get('/:email', async(req, res) => {
         try{
            const bookingEmail = req.params.email;
            const bookings = await bookingService.getBookingByEmail(bookingEmail);
            res.status(200).json({bookings:bookings});
         }catch(error){
              console.log(error.message);
              res.status(500).send({message:"Sorry we have some problems with the sever.please try later"})
         }
        
     })
     app.get('/:id', async (req, res) => {
       try
       {
         const bookingId = req.params.id;
         const booking = await bookingService.getBookingById(bookingId);
         res.status(200).json({booking:booking});
       }
       catch(error){
          console.log("Error" + error.message)
          res.status(500).send({message:"Sorry we have some problems with the sever.please try later"})
       }
     });
     
     app.post("/", async(req, res) => {
         try{
              const bookingPostData = req.body;
              bookingService.createNewBooking(bookingPostData);
              res.status(200).send({"message":"booking successfully done !!!"});
         }catch(error){
              console.log("Error" + error.message)
              res.status(500).send({message:"Sorry we have some problems with the sever.please try later"})
         }
     })
     app.post("/cancel",async(req, res) => {
          try{

              const {bookingId, email} = req.body;
              const arrayOfBookingToCancel = await bookingService.getBookingByIdAndEmail(bookingId,email);
              const isbookingFound = arrayOfBookingToCancel.length > 0 ? true : false;

              if(!isbookingFound){
                  res.send({message:"Booking matching id and email not found", status:404});
                  return;
              }

              const bookingToCancel = arrayOfBookingToCancel[0];
              cancelBooking.cancleBooking(bookingToCancel);

              res.send({message:"booking successfully canceled !!!!", status:200});

          }catch(error){
              console.log("error from booking cancel " + error);
              res.send({message:"Sorry we have some problems with the sever.please try later", status:500})
          }
         
     })
}