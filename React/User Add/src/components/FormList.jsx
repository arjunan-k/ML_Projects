import { useState } from 'react';
import './FormList.css'

const FormList = (props) => {
    const data = [{id: 1, name: "Arjun", age: 20}]
    
    const [name, setName] = useState("");
    const [age, setAge] = useState("");

    const userNameHandler = (e) => {
        setName(e.target.value)
    }

    const ageHandler = (e) => {
        setAge(e.target.value)
    }

    const buttonHandler = (e) => {
        e.preventDefault()
        data.push({'id': Math.random(),'name': name, 'age': age})
        setName("")
        setAge("")
        props.data(data)
    }

    return (
        <div>
            <form action="" className='formlist'>
                <label htmlFor="username">Username</label>
                <input type="text" name='username' onChange={userNameHandler} value={name}/>
                <label htmlFor="age">Age (Years)</label>
                <input type="number" name="age" onChange={ageHandler} value={age}/>
                <button type='submit' onClick={buttonHandler}>Add User</button>
            </form>
        </div>
    )
}

export default FormList;