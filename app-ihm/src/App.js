import BookingView from "./component/flight";
import BookingDetail from "./component/booking";
import 'bootstrap/dist/css/bootstrap.min.css';
import 'bootstrap/dist/js/bootstrap';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';


const App = () => {

    return ( 
        <Router>
            <Routes>
              <Route path="/" element=<BookingView/> />
              <Route exact path="booking/:email" element=<BookingDetail/> />
            </Routes>
        </Router>
     );
}
 
export default App;