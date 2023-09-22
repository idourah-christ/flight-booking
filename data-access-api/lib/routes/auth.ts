import { FlightController } from "../controllers/flight";
import * as express from "express";
import { Request, Response } from "express";
import {authenticateToken, generateToken} from "../middlewares/authentication";
import * as jsonwebtoken from "jsonwebtoken";
import { AuthController } from "../controllers/auth";


export class AuthRoutes{

    //public authController: AuthController = new FlightController();

    public routes(app:express.Application):void{
        
        app.route("/login")
        .post(generateToken, (req, res) => {
            // do auther things
        })

    }
}