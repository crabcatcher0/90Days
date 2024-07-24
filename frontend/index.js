// function Navbar() {
//     return (
//         <nav className="navbar navbar-expand-lg navbar-light bg-light">
//         <a className="navbar-brand" href="#">Navbar</a>
//         <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
//             <span className="navbar-toggler-icon"></span>
//         </button>

//         <div className="collapse navbar-collapse" id="navbarSupportedContent">
//             <ul className="navbar-nav mr-auto">
//                 <li className="nav-item active">
//                 <a className="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
//             </li>
//             <li className="nav-item">
//                 <a className="nav-link" href="#">Link</a>
//             </li>
//             <li className="nav-item dropdown">
//                 <a className="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
//                 Dropdown
//                 </a>
//             <div className="dropdown-menu" aria-labelledby="navbarDropdown">
//                 <a className="dropdown-item" href="#">Action</a>
//                 <a className="dropdown-item" href="#">Another action</a>
//                 <div className="dropdown-divider"></div>
//                     <a className="dropdown-item" href="#">Something else here</a>
//                 </div>
//             </li>
//             <li className="nav-item">
//                 <a className="nav-link disabled" href="#">Disabled</a>
//             </li>
//             </ul>
//         </div>
//         </nav>
//     )
// }

// function MainContent() {
//     return (
//        <p>Hi, This is MainContent.</p>
//     )
// }

// ReactDOM.render(
//     <div>
//         <Navbar/>
//         <MainContent/>
//     </div>,
//     document.getElementById("root")
// )

const navbar = (
    <div>
        <nav>
            <span>BrandName</span>
            <ul>
                <li>About</li>
                <li>Contact</li>
                <li>Pricing</li>
            </ul>
        </nav>
    </div>
)

ReactDOM.render(navbar, document.getElementById("root"))