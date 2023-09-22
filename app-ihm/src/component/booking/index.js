import {useParams} from 'react-router-dom';
import { useEffect, useState } from 'react';
import { axiosInstance } from '../../axios';
import {Alert} from '@mui/material';

const BookingDetail = () => {

    const [bookings, setBooking] = useState(null);
    const [isCanceled, setIsCanceled] = useState(false);

    const {email} = useParams();

    useEffect(() => {
        axiosInstance.get(`booking/${email}`).then(res => {
            const {bookings} = res.data;
            setBooking(bookings)
        }).catch(error => {
            console.log(error);
        })
    },[email]);

    const handleCancelClicked = (event) => {
        const cancelData = {"bookingId":event.target.id, "email":email};
        axiosInstance.post("booking/cancel", cancelData).then(res => {
            setIsCanceled(true);
        }).catch(error => {
            console.log(error);
        })
    }
    return ( 
     
        <div className="container mt-3">
            { isCanceled ?<Alert onClose={() => setIsCanceled(false)} severity="success">Booking successfully canceled !</Alert>:null }
           
            {bookings && 
                bookings.map((booking, index) =>  
                <div className="card mt-3" key={index}>
                    <div className="card-header">
                        <h3>Booking Informations:</h3>
                    </div>
                    <div className="card-body">
                        <h5>Flight Id: {booking.flight}</h5>
                        <h5>Currency: {booking.currency.currency}</h5>
                        <h5>Price: {booking.price}</h5>
                        <h5>Date: {booking.date}</h5>
                        <h5>Extra laguage: {booking.extraLaguageNumber}</h5>
                    </div>
                    <div className="card-footer">
                        <button onClick={handleCancelClicked} id={booking.id} className="btn btn-danger">Annuler</button>
                    </div>
                </div>)
            }
        </div>
     );
}
 
export default BookingDetail;