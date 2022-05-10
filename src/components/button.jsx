import './button.css'
import './label.css'


const Button = (props) => {
    let label;
    if (props.label !== undefined)
        label = <label htmlFor={props.name}> {props.label} </label>
    
    return (<>
        {label}
        <button onClick={props.onClick}> {props.name}</button>
    </>)
}
export default Button ;