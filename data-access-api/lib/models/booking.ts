import * as mongoose from "mongoose";

const Schema = mongoose.Schema;

export const BookingSchema = new Schema({
    flight:{
        type:String
    },
    date:{
        type:String
    },
    extraLaguage:{
        type:Number
    },
    currency:{
        type:String
    }
})