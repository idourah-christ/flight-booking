import * as mongoose from "mongoose";
import { Request, Response } from "express";
import FlightModal, {IFlight} from "../models/flight";

const bookings : any[] = [];

export class BookingController {
   
    public async add(req:Request, res:Response) :Promise<void>{
        try
        {
            let booking:any = req.body;
            bookings.push(booking);
            res.status(201)

        }catch(error)
        {
            console.log(error);
            res.status(500).json({error:"Error creating booking"});
        }
    }

    public async all(req:Request, res:Response) : Promise<void>{
        try
        {
            res.status(200).send(bookings);
        }
        catch(error)
        {
            console.log(error);
            res.status(500).json({error:"Error retreiving bookings"});
        }
    }

    public async getWithId(req:Request, res:Response) : Promise<void>{
        try
        {
            const bookingId = parseInt(req.params.id);
            const filteredBookings = bookings.filter((obj) => obj.id === bookingId);
            res.status(200).send(filteredBookings[0]);
        }
        catch(error)
        {
            console.log(error);
            res.status(500).json({error:"Error retreiving flight by Id"});
        }
    }
}