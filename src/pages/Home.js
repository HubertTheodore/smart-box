import "../App.css";
import {Field} from "../components/Field";
import {Inputs} from "../components/Inputs.js";
import {Ball} from "../components/Ball.js";
import {useState} from "react";

// incorporates the all the html on Home
export const Home = () => { 
    const [objectIn, setObjectIn] = useState(false)

    return ( 
        <div>
            <h1>The Smart Box</h1> {/* header for title of project */}
            <div className="HomeComponents"> {/* encompasses all of the components on home page */}
               <div className="FieldAndInputs"> {/* encompasses the field and input components */}
                <Field />
                <Inputs setObjectIn={setObjectIn}/>
                </div>
                <div> {/* encompasses the component that tells us if object is caught */}
                    <Ball objectIn={objectIn}/>
                </div> 
            </div>
        </div>
    );
}

