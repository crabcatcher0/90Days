import { useState } from "react";

export default function Counter() {
    const [count, setCount] = useState(0);

    function plusClick() {
        setCount(count + 1);
    }
    function minusClick() {
        setCount(count -1);
    }
    return (
        <div>
            <h1>Count Value is: {count}</h1>
            <button onClick={plusClick}>Increment</button>
            <button onClick={minusClick}>Decrement</button>
        </div>
    );
}
