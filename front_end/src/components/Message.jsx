export default function Message() {
    function handleClick() {
        console.log("Button clicked.");
    }
    return (
        <div>
            <button onClick={handleClick}>Click here to get a message.</button>
        </div>
    );
}