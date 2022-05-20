import "./table.css";

const URLTable = (props) => {
    if (props.data === undefined || props.data.length === 0)
     return <div id="table" className="ErrMessage">No data found</div>

   const header = Object.keys(props.data[0]);
   return (<table className="urlTable">
        <thead>
            <tr>
                {header.map(h => <th>{h}</th>)}
            </tr>
        </thead>
        <tbody>
            {props.data.map(v =>
            <tr>
                {header.map(key =><td>{v[key]}</td>)}
            </tr>)}
        </tbody>
    </table>)
}   

export default URLTable;