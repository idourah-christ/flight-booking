import {Request, Response, NextFunction } from "express";
import * as jwt from "jsonwebtoken";

export function generateToken(req:Request, res:Response, next:NextFunction){
    const {email, password} = req.body;

    const user = {
        email:email,
        password:password
    }
    jwt.sign({user:user}, "secretkey", (err:any, token:any) => {
        if(err){
            res.status(500).json({message:"Error could not login"});
        }
        res.status(200).json({token:token});
    })
    next();
}

export function authenticateToken(req:Request, res:Response, next:NextFunction){

    const bearerHeader = req.header("Authorization");

    if(!bearerHeader){
        return res.status(401).json({message:"Authentication failed. No token provided."})
    }

    const bearer = bearerHeader.split(' ');

    const token = bearer[1];

    jwt.verify(token,'secretkey' as string, (err, user) => {

        if(err){
            return res.status(403).json({message:"Authentication failed. Invalid token"})
        }

        // (req as any).user = user; 

        next();
    })
}