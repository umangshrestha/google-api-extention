import {useRef} from 'react';


const style = {
    backgroundColor: "#04AA6D",
    color: "black",
    padding: "20px",
    textAlign: "center",
    textDecoration: "none",
    display: "inline-block",
    fontSize: "16px",
    margin: "4px 2px",
    borderRadius: "12px",
}

const Uploader = (props) => {
    const fileInputRef =useRef();
    return <>
        <input type="file" id={props.id} name={props.id} multiple="multiple" ref={fileInputRef} onChange={props.func} hidden/> 
        <button onClick={()=>fileInputRef.current.click()} style={style}> {props.text} </button>
    </>
}


export default Uploader