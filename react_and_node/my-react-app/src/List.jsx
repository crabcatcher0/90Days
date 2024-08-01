

function List() {

    const fruits = [
        {id: 1, name:"apple", calories: 95}, 
        {id: 2, name:"orange", calories: 76}, 
        {id: 3, name:"banana", calories: 98},
        {id: 4, name:"coconut", calories: 23}
    ];

    fruits.sort((a, b) => a.name.localeCompare(b.name))
    
    
    const listitems = fruits.map(fruit => <li key={fruit.id}>{fruit.name}: &nbsp;
    {fruit.calories}</li>)
    return (
        <ol>{listitems}</ol>
    );
}

export default List;