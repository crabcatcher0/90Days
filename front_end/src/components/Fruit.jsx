export default function Fruit({name, price, emoji, soldout}){
    return (
    <>
        <li>
            {emoji} {name} ${price} {soldout ? "(soldout)":""}
        </li>  
    </>
    );
}