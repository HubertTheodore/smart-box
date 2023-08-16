import "../App.css";

// displays the component that tells us if object has been caught in box
export const Ball = ({objectIn}) => {
    return (
        <div className= 'BallText' > 
            <p> Green = Object In </p> 
            <p> Red = Object Not in </p>
            <div className={`BallIndicator ${objectIn ? 'BallIndicator-Green' : 'BallIndicator-Red'}`} > {/* logic for turning circle green or red depending if object is caught or not */}
            </div> 
        </div> 
    );
}

