import './App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import {Home} from "./pages/Home";
import {About} from "./pages/About";
import {Software} from "./pages/Software";
import {Hardware} from "./pages/Hardware";
import {Navbar} from "./components/Navbar";

// encompasses everything on the webpage, sets up routing for different pages
function App() {
  return (
    <Router>
      <Navbar />
      <Routes>
        <Route path="/" element={<Home />}/> 
        <Route path="/about" element={<About />}/>
       {/* <Route path="/software" element={<Software />}/>
        <Route path="/hardware" element={<Hardware />}/>*/}
      </Routes>
    </Router>
  );
}

export default App;
