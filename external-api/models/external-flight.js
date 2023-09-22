class ExternalFlightModel {

    constructor(){
        this.flight = null;
        this.date = null;
        this.extraLaguageNumber = 0;
        this.currency = "EUR"
        this.id = this.getRandomId(2, 40);
        this.email = null;
        this.status = null;
    }

    setFlight(flight){
        this.flight = flight
    }
    setBookingDate(date){
        this.date = date
    }
    setExtraLaguageNumber(extraLaguageNumber){
        this.extraLaguageNumber = extraLaguageNumber
    }
    setCurrency(currency){
        this.currency = currency;
    }
    getRandomId(min, max) {
        min = Math.ceil(min);
        max = Math.floor(max);
        return Math.floor(Math.random() * (max - min)) + min;
    }
    setEmail(email){
        this.email = email
    }
    status(status){
        this.status = status;
    }
}

module.exports = ExternalFlightModel