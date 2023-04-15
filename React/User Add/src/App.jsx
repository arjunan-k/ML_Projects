import './App.css'
import FormList from './components/FormList'
import UserData from './components/UserData'
import { useState } from 'react';

function App(props) {

  let allData = [{id: 2, name: "ArjunanK", age: 20}];

  const dataHandler = (data) => {
    allData = [...data]
  }

  return (
    <div>
      <div className='container'>
        <FormList data={dataHandler}/>
      </div>
      <div className='container'>
        <UserData userData={allData} />
      </div>
    </div>
  )
}

export default App