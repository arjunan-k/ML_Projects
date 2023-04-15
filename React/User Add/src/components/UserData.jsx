import './UserData.css'

const UserData = (props) => {

    return (
        <div>
            {props.userData.map(data => <div className='card' key={data.id}>{data.name} {data.age}</div>)}
        </div>
    )
}

export default UserData;