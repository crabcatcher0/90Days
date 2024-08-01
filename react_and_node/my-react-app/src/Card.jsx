import profilePic from './assets/profile.jpeg'

function Card() {
    return (
        <div className="card">
            <img className="card-img" src={profilePic} alt="profile picture"></img>
            <h2 className="card-title">My SIte</h2>
            <p className="card-text">I am learning also i want to know react.</p>
        </div>
    );
}

export default Card;