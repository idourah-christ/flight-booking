const Booking = require("../models/booking");
const axiosInstance = require("../axios");


class BookingService{

    async getAllBooking(){
        try{
            const response = await axiosInstance.get("booking");
            return response.data;

        }catch(error){
            console.log(error);
            throw Error("GetAllBookingException error: " + error);
        }     
    }

    async getBookingById(bookingId){
        try{
            const response = await axiosInstance.get('booking/'+bookingId);
            return response.data;

        }catch(error){
            console.log("Error get booking by id", error);
            throw Error("GetByIdException error: " + error);
        }
    }
    
    createNewBooking(bookingPostData){
       try
       {
            const booking = new Booking();
            booking.setFlight(bookingPostData["flight"]);
            booking.setCurrency(bookingPostData["currency"] || "EUR");
            booking.setExtraLaguageNumber(bookingPostData["laguage"] || 0);
            booking.setBookingDate(bookingPostData["date"]);
            booking.setEmail(bookingPostData["email"])
            axiosInstance.post("booking", booking);

       }catch(error){
            console.log("Error when creating booking " + error)
            throw Error("CREATE_NEW_BOOKING_EXCEPTION");
       }
    }
    async getBookingByEmail(bookingEmail){
        try{
            const response = await axiosInstance.get("booking");
            const bookings = response.data;
            const filteredBookings = bookings.filter((obj) => obj.email === bookingEmail);
            return filteredBookings;

        }catch(error){
            throw Error("GET_BOOKING_BY_EMAIL_EXCEPTION" + error)
        }
       
    }
    async getBookingByIdAndEmail(bookingId, bookingOwnerEmail){
        try{
            const bookingsByEmail = await this.getBookingByEmail(bookingOwnerEmail);
            const isbookingFound = bookingsByEmail.length > 0 ? true : false;
            
            if(isbookingFound){
                const matchingBooking = bookingsByEmail.filter((booking) => booking.id === bookingId);
                return matchingBooking;
            }
            return [];
        }
        catch(error){
            console.log(error.message)
            throw Error("GET_BOOKING_BY_ID_AND_EMAIL_EXCEPTION" + error.message);
        }
    }
}

module.exports = BookingService;