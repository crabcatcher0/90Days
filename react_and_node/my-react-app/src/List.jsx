

function List() {

    const fruits = ["apple", "orange", "banana", "coconut"];
    fruits.sort()
    const listitems = fruits.map(fruit =><li>{fruit}</li>)
    return (
        <ol>{listitems}</ol>
    )
}

export default List;