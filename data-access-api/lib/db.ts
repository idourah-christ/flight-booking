import * as mongoose from 'mongoose';

export class Database{

    public mongoUrl: string = 'mongodb://127.0.0.1/booking';

    public async connect():Promise<void>{

        try{
            await mongoose.connect(this.mongoUrl);
            console.log("connect sucessfull to " + this.mongoUrl)
        }
        catch(error){
            console.log(error);
        }
    }
}