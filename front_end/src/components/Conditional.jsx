import Code from "./Code";
import Welcome from "./Welcome";

export default function Conditional() {
    const display = true;
    return display ? <Welcome /> : <Code />;
}