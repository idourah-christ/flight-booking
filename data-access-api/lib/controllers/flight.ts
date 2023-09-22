import * as mongoose from "mongoose";
import { Request, Response } from "express";
import FlightModal, {IFlight} from "../models/flight";

export class FlightController {

    public async add(req:Request, res:Response) :Promise<void>{
        try
        {
            let {title, price, places} = req.body;
            let newFlight:IFlight = new FlightModal({title, price, places});

            let savedFlight = await newFlight.save();
            res.status(201).json(savedFlight);

        }catch(error)
        {
            console.log(error);
            res.status(500).json({error:"Error creating flight"});
        }
    }

    public async all(req:Request, res:Response) : Promise<void>{
        try
        {
            let fligths = await FlightModal.find();
            res.status(200).json(fligths);
        }
        catch(error)
        {
            console.log(error);
            res.status(500).json({error:"Error retreiving flights"});
        }
    }

    public async getWithId(req:Request, res:Response) : Promise<void>{
        try
        {
            const fligthId = req.params.id;
            let flight = await FlightModal.findById(fligthId);
            res.status(200).json({data:flight});
        }
        catch(error)
        {
            console.log(error);
            res.status(500).json({error:"Error retreiving flight by Id"});
        }
    }
}