import BookingForm from "./form";
import { axiosInstance } from "../../axios";
import { useEffect, useState } from "react";

const BookingView = () => {

    const [state, setState] = useState(null);

    useEffect(() => {
      
      axiosInstance.get('flight').then(response => {
            setState(response.data);
        }).catch(err => {
          console.log(err);
        }); 

    }, [])
    return ( 
        <div className="container">
             {state && <BookingForm state={state}/>}
        </div>
     );
}
 
export default BookingView;