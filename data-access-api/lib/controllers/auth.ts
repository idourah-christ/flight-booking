import { Request, Response } from "express";


export class AuthController {

    public async login(req:Request, res:Response) :Promise<void>{
        res.status(200).json({message:"Welcome to login"});
    }
}