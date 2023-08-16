import "../App.css";
import LeftArrow from "../images/left_arrow.png";
import RightArrow from "../images/right_arrow.png";
import UpArrow from "../images/up_arrow.png";
import DownArrow from "../images/down_arrow.png";
import {useState} from "react";

// component for all input related components
export const Inputs = ({setObjectIn}) => {
    // state variables
    const [x, setX] = useState("");
    const [y, setY] = useState("");
    const [isValidX, setIsValidX] = useState(false);
    const [isValidY, setIsValidY] = useState(false);
    const [isMoving, setIsMoving] = useState(false);

    // coordinate boundaries
    const minX = 3;
    const minY = 3;
    const maxX = 14;
    const maxY = 12;

    const getX = (val) => { // determines if the value in the input box is valid and then sets the x value
        setX(val.target.value);
        if(val.target.value === "" || val.target.value === null || val.target.value < minX || val.target.value > maxX || !/^\d*(\.\d+)?$/.test(val.target.value)) {
            setIsValidX(false)
        } else {
            setIsValidX(true)
        }
    }

    const getY = (val) => { // determines if the value in the input box is valid and then sets the y value
        setY(val.target.value);
        if(val.target.value === "" || val.target.value === null || val.target.value < minY || val.target.value > maxY || !/^\d*(\.\d+)?$/.test(val.target.value)) {
            setIsValidY(false)
        } else {
            setIsValidY(true)
        }
    }

    // sends the valid x and y data to the backend through a post request
    const sendCoordsToBackEnd = async () => { 
        const data = {
            x: x, 
            y: y,
            direction: "",
        }; 

        try {
            const response = await fetch("http://cpen291-28.ece.ubc.ca/api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
            });    
            console.log(response)

            {(response.status === "undefined" || response.status === "busy") ? setIsMoving(true) : setIsMoving(false)}
            {(response.object === "undefined" || response.object === "false") ? setObjectIn(false) : setObjectIn(true)}
        } catch(err) {
            console.error()
        }
    }
    
    // send direction to backend through a post request
    const sendDirectionToBackEnd = async (direction) => { // sends a direction to the backend through a post request
        const data = {
            x: "", 
            y: "",
            direction: direction,
        }; 
    
        try {
            const response = await fetch("http://cpen291-28.ece.ubc.ca/api", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
            });    
            console.log(response)

            {(response.status === "undefined" || response.status === "busy") ? setIsMoving(true) : setIsMoving(false)}
            {(response.object === "undefined" || response.object === "false") ? setObjectIn(false) : setObjectIn(true)}
        } catch(err) {
            console.error()
        }
    }

    return ( // all the input components together
        <div className="Inputs">
            <div className="HorizontalArrows">
                <button><img src={LeftArrow} alt="left arrow" onClick={() => {!isMoving && sendDirectionToBackEnd("left")}}></img></button>
                <div className="VerticalArrows">
                    <button><img src={UpArrow} alt="up arrow" onClick={() => {!isMoving && sendDirectionToBackEnd("up")}}></img></button>
                    <button><img src={DownArrow} alt="down arrow" onClick={() => {!isMoving && sendDirectionToBackEnd("down")}}></img></button>  
                </div>                                                                         
                <button><img src={RightArrow} alt="right arrow" onClick={() => {!isMoving && sendDirectionToBackEnd("right")}}></img></button>           
            </div>
            {isMoving ? <div>The box is still moving. Any requests to move will not be accepted now.</div> : <div>You can make a request to move.</div>}
            <div className="XYInputs">
                <div className="TextBoxes">
                    <h2>X value</h2>
                    <input type="text" onChange={getX}/>
                    {!isValidX && <div> Enter an x value from {minX} - {maxX} </div>} {/* warns user by text if X value is invalid */}
                </div>
                <div className="TextBoxes"> 
                    <h2>Y value</h2>
                    <input type="text" onChange={getY}/>
                    {!isValidY && <div> Enter a y value from {minY} - {maxY} </div>} {/* warns user by text if Y value is invalid */}
                </div>
            </div>
            <div>
                <button onClick={() => {
                    (isValidX && isValidY && !isMoving) && sendCoordsToBackEnd() // only send data to backend if coords are valid and box is not moving
                    }}>Confirm X and Y coordinates</button> 
            </div>
        </div>
    );
} 
