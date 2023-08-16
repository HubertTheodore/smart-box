import "../App.css";
import {NavbarData} from "./NavbarData";

// the navbar as a whole
export const Navbar = () => {
    return (
    <div className="Navbar">
        <ul className="NavbarList"> 
          {NavbarData.map((val, key) => { {/* lists all the navbar items in the navbar */}
            return (
            <li key={key} className="row" onClick={() => {
                window.location.pathname = val.link; // clicking navbar item goes to that window
            }}>
                <div>{val.icon}</div><div>{val.title}</div> {/* displays the icon and title of the navbar elements */}
            </li>);
            })}  
        </ul>
    </div>
    );
}