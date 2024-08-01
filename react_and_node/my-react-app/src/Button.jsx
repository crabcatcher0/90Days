
function Button() {

    const handleClick = (e) => console.log(e);

    return (
        <button className="button" onClick={(e) => handleClick(e)}>Click Me</button>
    );
}

export default Button;