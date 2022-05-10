import './button.css'

const Button = (props) => <button onClick={props.onClick}> {props.name}</button> 

export default Button;