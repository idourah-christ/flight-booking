export default class Calcultor{

    totalFlightPriceToPay(flightPrice, extraLaguageNumber){
        return flightPrice * this.totalLaguageFeesToPay(extraLaguageNumber);
    }
    totalLaguageFeesToPay(extraLaguageNbr){
        return extraLaguageNbr > 0 ? extraLaguageNbr * 100 : 1; 
    }
    
    priceOnDiscount(price, discount){
        return price - ((price / 100) * discount);
    }

    convertPrice(basePrice, currencyValue){
        let price = basePrice * currencyValue;
        return Math.round(price * 100) / 100;
    }
}
