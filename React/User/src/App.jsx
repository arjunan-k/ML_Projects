import './App.css'
import AddUser from './components/Users/AddUser'
import UserList from './components/Users/UserList'
import { useState } from 'react';

function App(props) {

  const [usersList, setUsersList] = useState([])

  const addUserDataHandler = (uName, uAge) => {
    setUsersList(prevData => {
      return [...prevData, {id: Math.random().toString(), name: uName, age: uAge}]
    })
  }

  return (
    <div>
      <AddUser onAddUser={addUserDataHandler}/>
      <UserList users={usersList}/>
    </div>
  )
}

export default App