import * as express from "express";
import * as bodyParser from "body-parser";
import * as dotenv from "dotenv";
import * as cors from 'cors';

import { FlightRoutes } from "./routes/flight";
import { AuthRoutes } from "./routes/auth";
import { Database } from "./db";
import { BookingRoutes } from "./routes/booking";


class App{

    public app: express.Application;
    public flightRoutes: FlightRoutes =  new FlightRoutes();
    public authRoutes: AuthRoutes = new AuthRoutes();
    public bookingRoutes: BookingRoutes = new BookingRoutes()
    public database = new Database();

    constructor(){
        this.app = express();
        this.config();
        this.mongoSetup();
        dotenv.config();

        this.flightRoutes.routes(this.app);
        this.authRoutes.routes(this.app);
        this.bookingRoutes.routes(this.app);
    }

    private config(): void {
        this.app.use(bodyParser.json());
        this.app.use(bodyParser.urlencoded({extended:false}));
        this.app.use(cors());
    }

    private mongoSetup():void{
        this.database.connect();
    }
}

export default new App().app