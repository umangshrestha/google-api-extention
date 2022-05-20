import './countTable.css';
import RemoveButton from './removeButton';


const CountTable = (props) => (
    <table>
        <thead>
            <tr>
                <th onClick={()=>props.onClick("url")}>Url Count</th>
                <th onClick={()=>props.onClick("auth")}>Json Count</th>
                <th onClick={()=>props.onClick("status")}>Processed Count</th>
                <th onClick={()=>props.onClick("success")}>Success Count</th>   
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>{props.data.url}<RemoveButton onClick={()=> props.remove("url")}/></td>
                <td>{props.data.json}<RemoveButton onClick={()=> props.remove("auth")}/></td>
                <td>{props.data.processed}<RemoveButton onClick={()=> props.remove("status")}/></td>
                <td>{props.data.success}<RemoveButton onClick={()=> props.remove("success")}/></td>
            </tr>
        </tbody>
    </table>
)

export default CountTable;