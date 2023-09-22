import mongoose, {Document, Schema} from 'mongoose';

export interface IFlight extends Document{
    title:string
    price:number,
    places:number;
    createdDate:Date
}

export const flightSchema: Schema<IFlight> = new mongoose.Schema({
    title:{
        type:String,
        required:true,
        unique:true
    },
    price:{
        type:Number
    },
    places:{
        type:Number
    },
    createdDate:{
        type:Date,
        default:Date.now
    }
});


const FlightModel = mongoose.model<IFlight>("Flight", flightSchema);

export default FlightModel;