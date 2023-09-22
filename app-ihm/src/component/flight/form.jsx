import { Component } from "react";
import { axiosInstance } from "../../axios";
import "./form.css"
import Calcultor from "./calculator";

class BookingForm extends Component{

    constructor(props){
        super(props)

        this.flights = props.state.flights;
        this.currencies = props.state.currencies;
        this.flightCalulator = new Calcultor();
        let {price, places} = this.flights[0]
        let totalPrice = this.flightCalulator.totalFlightPriceToPay(price, 0);

        this.state = {
            flight:0,
            price:price,
            places:places,
            date:"",
            selectedCurrency:0,
            laguage:0,
            totalPrice:totalPrice,
            passengers:0,
            isDiscountApplied:false,
            email:""
        }
    }

    handleOnChange = (event) => {
        this.setState({
            ...this.state,
            [event.target.name]:event.target.value
        }) 
    }

    handleOnPassengerChange = (event) => {

        const passengerNumber = parseInt(event.target.value);
       
        let totalPrice = this.state.totalPrice;
       
        if(passengerNumber === 10){
            totalPrice = this.flightCalulator.priceOnDiscount(this.state.totalPrice, 10);
           
        }
        this.setState({
            ...this.state,
            passengers:passengerNumber,
            totalPrice:totalPrice,
        });
    }
   
    handleCurrencyChange = (event) => {
        const index  = event.target.value;
        const currentPrice = this.getConvertedPrice(this.state.price, index);
        const totalPrice = this.flightCalulator.totalFlightPriceToPay(currentPrice, this.state.laguage);
        this.setState({
            ...this.state,
            price:currentPrice,
            selectedCurrency:index,
            totalPrice:totalPrice
        })
    }
    getConvertedPrice = (currentPrice, seletedCurrencyIndex) => {
        let selectedCurrencyValue = this.currencies[seletedCurrencyIndex].value;
        return this.flightCalulator.convertPrice(currentPrice, selectedCurrencyValue)
    }   
     
    hanleFlightChanged = (event) => {
        let seletedFlight = event.target.value;
        let flightPrice = this.flights[seletedFlight].price
        let seletedCurrency = this.state.selectedCurrency;
        const currentPrice = this.getConvertedPrice(flightPrice, seletedCurrency);
        this.setState({
            ...this.state,
            price:currentPrice,
            flight:seletedFlight,
            totalPrice:this.calculateTotalFlightPrice(currentPrice, this.state.laguage)
        })
        
    }
    handleOnSubmit = (event) => {
        event.preventDefault();
        const data = {
            "flight":this.flights[this.state.flight]._id,
            "date":this.state.date,
            "extraLaguageNumber":this.state.laguage,
            "currency":this.currencies[this.state.selectedCurrency],
            "price":this.state.price,
            "email":this.state.email
        };

        axiosInstance.post("booking", data).then(response => {
            console.log(response);
        })
        .catch(error => {
            console.log(error);
        })
    }
    handleOnLaguageChange = (event) => {
        let laguageNumber  = event.target.value;
        let totalPrice = this.flightCalulator.totalFlightPriceToPay(this.state.price, laguageNumber);
        this.setState({
            ...this.state,
            laguage:laguageNumber,
            totalPrice: totalPrice
        })
    }
    

    render(){
        return (
            <form onSubmit={this.handleOnSubmit} className="mt-4">

                <h1>Booking.com</h1>
                <div className="form-group mb-3">
                    <div className="row">
                        <div className="col-md-6">
                            <label htmlFor="">Vols: </label>
                            <select className="form-control border border-success"  value={this.state.flight} name="flight" onChange={this.hanleFlightChanged}>
                                {this.flights && 
                                    this.flights.map((flight, index) => <option key={index} value={flight._id}>{ flight.title }</option>)
                                }
                            </select>
                        </div>
                        <div className="col-md-6">
                            <label htmlFor="">Devises: </label>
                            <select className="form-control border border-primary"  value={this.state.selectedCurrency} name="currency" onChange={this.handleCurrencyChange}>
                                <option value="1">EUR</option>
                                {this.currencies && 
                                    this.currencies.map((item, index) => <option key={index} value={index}>{ item.currency }</option>)
                                }
                            </select>
                        </div>
                    </div>
                </div>
            
                <div className="form-group mt-2">
                    <div className="row">
                        <div className="col-md-6">
                            <label htmlFor="">Departure Date:</label>
                            <input type="date" name="date" value={this.state.date} onChange={this.handleOnChange} className="form-control border border-success"/>
                        </div>
                        <div className="col-md-6">
                            <label htmlFor="">Extra laguage:</label>
                            <input type="number" className="form-control border border-primary" name="laguage" value={this.state.laguage} onChange={this.handleOnLaguageChange} />
                        </div>
                    </div>
                </div>

                <div className="form-group mt-3">
                    <div className="row">
                        <div className="col-md-6">
                            <label className="form-label">Flight Price:</label>
                            <input type="text" className="form-control border border-success" name="price" readOnly value={this.state.price} defaultValue={this.state.price}/>
                        </div>
                        <div className="col-md-6">
                            <label className="form-label">Passenger Number:</label>
                            <input type="number" className="form-control border-primary" name="passengers" onChange={this.handleOnPassengerChange} value={this.state.passengers} defaultValue={this.state.passengers}/>
                        </div>
                    </div>
                </div>
                <div className="form-group mt-3">
                    <label className="form-label">Email</label>
                    <div className="col-md-12">
                        <input type="email" className="form-control border-primary" name="email" onChange={this.handleOnChange} value={this.state.email}/>
                    </div>
                </div>
                <hr></hr>
                <div>
                    <h6>Total Price: <span className="text-success">{this.state.totalPrice}</span></h6>
                </div>

                
                <div className="form-group mt-3">
                    <button className="btn btn-primary" type="submit">Book</button>
                </div>
                
            </form>
        )
    }

}


export default BookingForm;