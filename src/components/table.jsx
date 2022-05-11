import './table.css';

const Table = (props) => (
    <table>
        <thead>
            <tr>
                <th>#</th>
                <th>Key Phrase</th>
                <th>Time</th>
                <th>Status</th>
            </tr>
        </thead>
        <tbody>
            {props.details.map((row, pos) => (<tr>
                <td>{pos+1}</td>
                <td>{row.url}</td>
                <td>{row.time}</td>
                <td>{row.status}</td>
            </tr>))}
        </tbody>   
    </table>
)

export default Table;