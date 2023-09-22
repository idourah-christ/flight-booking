const axiosInstance = require("../axios");
const {BookingService} = require("../services");

module.exports = class CancelBooking{

    constructor(){
        this.canceledBookingQueue = []
    }

    cancleBooking(booking){
        try{
           
            booking.status('CANCEL');
            this.pushBookingToQueue(booking);
            
        }catch(error){
            console.log(error.message)
        }
    }
    
    pushBookingToQueue(booking){
        this.canceledBookingQueue.push(booking);
    }
    getCancledBooking(){
        return this.canceledBookingQueue;
    }
}