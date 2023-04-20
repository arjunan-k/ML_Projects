import Card from "../UI/Card";
import styles from './AddUser.module.css'
import Button from "../UI/Button";
import { useState, useRef } from "react";
import ErrorModal from './../UI/ErrorModal';
import React from "react";
import { Fragment } from "react";

const AddUser = props => {

    const [error, setError] = useState()


    const [enteredUserName, setEnteredUserName] = useState("")
    const [enteredAge, setEnteredAge] = useState("")
    const nameInputRef = useRef();
    const ageInputRef = useRef();

    const userNameChangeHandler = (e) => {
        setEnteredUserName(e.target.value)
    }

    const ageChangeHandler = (e) => {
        setEnteredAge(e.target.value)
    }

    const addUserHandler = (e) => {
        e.preventDefault();
        console.log(nameInputRef)
        console.log(nameInputRef.current.value)
        const enteredName = nameInputRef.current.value
        const enteredUserAge = ageInputRef.current.value

        if(enteredUserName.trim().length === 0 || enteredAge.trim().length === 0) {
            setError({title: "Invalid Input", message: "please enter a valid non-empty name & age."})
            return
        }

        if(+enteredAge < 1) {
            setError({title: "Invalid Input", message: "please enter a valid age greater than zero."})
            return
        }

        props.onAddUser(enteredUserName, enteredAge)
        // props.onAddUser(enteredName, enteredUserAge)
        // nameInputRef.current.value = ""
        // ageInputRef.current.value = ""


        setEnteredUserName("")
        setEnteredAge("")
    }

    const errorHandler = () => {
        setError(null)
    }

    return (
        <React.Fragment>
        <Fragment>
            {error && <ErrorModal title={error.title} message={error.message} onConfirm={errorHandler}/>}
            <Card className={styles.input}>
                <form action="">
                    <label htmlFor="username">UserName</label>
                    <input type="text" id="username" value={enteredUserName} onChange={userNameChangeHandler} ref={nameInputRef}/>
                    <label htmlFor="age">Age (Years)</label>
                    <input type="number" id="age" value={enteredAge} onChange={ageChangeHandler} ref={ageInputRef}/>
                    <Button onClick={addUserHandler} type="submit">Add User</Button>
                </form>
            </ Card>
        </Fragment>
        </React.Fragment>
    )
}

export default AddUser;