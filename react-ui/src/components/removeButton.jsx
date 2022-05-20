const style = {
    backgroundColor: "red",
    color: "black",
    padding: "2px",
    textAlign: "center",
    textDecoration: "none",
    display: "inline-block",
    fontSize: "10px",
    margin: "4px 2px",
    borderRadius: "12px",
}
const RemoveButton = (props) =>  <button onClick={props.onClick} style={style}> {props.text} </button>

export default RemoveButton;