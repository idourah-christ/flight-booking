import { BookingController } from "../controllers/booking";
import * as express from "express";
import { Request, Response } from "express";
import {authenticateToken} from "../middlewares/authentication";
import * as jsonwebtoken from "jsonwebtoken";


export class BookingRoutes{

    public bookingController: BookingController = new BookingController();

    public routes(app:express.Application):void{
        
        app.route("/")
        .get((req, res) => {
            res.status(200).send({
                message:"GET request successfull on booking service !!!!"
            })
        })

        app.route("/booking")
        .get(this.bookingController.all)
        .post(this.bookingController.add)

        app.route('/booking/:id')
        .get(this.bookingController.getWithId)
    }
}