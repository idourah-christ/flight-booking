import { FlightController } from "../controllers/flight";
import * as express from "express";
import { Request, Response } from "express";
import {authenticateToken} from "../middlewares/authentication";
import * as jsonwebtoken from "jsonwebtoken";


export class FlightRoutes{

    public flightController: FlightController = new FlightController();

    public routes(app:express.Application):void{
        
        app.route("/")
        .get((req, res) => {
            res.status(200).send({
                message:"GET request successfull !!!!"
            })
        })

        app.route("/flight")
        .get(this.flightController.all)
        .post(this.flightController.add)

        app.route('/flight/:id')
        .get(this.flightController.getWithId)
    }
}