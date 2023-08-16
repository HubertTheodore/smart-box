import "../App.css";
import Project from "../images/project.png";

// the about page content
export const About = () => { 
    return (
    <div>
       <h1>The Project</h1>
        <div className="box">
            The project is revolved around a metal box that is able to catch 
            falling objects within a boundary by taking inputs through a webpage to control
            where the box should go. This can be done by pressing arrows keys 
            to move it a fixed distance in the desired direction or by entering coordinates. 
        </div> 
        <div className="box">
            A picture of the project can be seen below.
        </div>
        <div className="box">
            <img src={Project} alt="project"></img>
        </div>
    </div>
    
    )
}

