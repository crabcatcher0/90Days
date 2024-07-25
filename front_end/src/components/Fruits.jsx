import Fruit from "./Fruit";

export default function Fruits() {

    // const fruits = ["Apple", "Banana", "Grapes", "Orange"]
    const fruits = [
        {
            name:"Apple",
            price: 10,
            emoji:"🍎",
            soldout:true
        },
        {
            name:"Mango",
            price: 13.5,
            emoji:"🥭",
            soldout:true
        },
        {
            name:"Banana",
            price: 12,
            emoji:"🍌",
            soldout:false
        },
        {
            name:"Orange",
            price: 3,
            emoji:"🍊",
            soldout:true
        }
    ];
    return (
    <div>
        <ul>
            {fruits.map(fruit => 
            <Fruit 
            key={fruit.name} 
            name={fruit.name} 
            price={fruit.price} 
            emoji={fruit.emoji}
            soldout={fruit.soldout} />
        )}
        </ul>
    </div>
    );
}