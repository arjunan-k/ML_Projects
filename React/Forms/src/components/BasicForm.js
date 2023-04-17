import useMineInput from './../hooks/user-mine-input';

const isNotEmpty = value => value.trim() !== ""
const isEmail = value => value.includes('@')

const BasicForm = (props) => {

  const {
    value: enteredName,
    isValid: enteredNameIsValid,
    hasError: nameInputHaserror, 
    valueChangeHandler: nameInputChangeHandler, 
    valueBlurHandler: nameInputBlurHandler,
    reset: resetNameInput 
  } = useMineInput(isNotEmpty)

  const {
    value: enteredLastName,
    isValid: enteredLastNameIsValid,
    hasError: lastNameInputHaserror, 
    valueChangeHandler: lastNameInputChangeHandler, 
    valueBlurHandler: lastNameInputBlurHandler,
    reset: resetLastNameInput 
  } = useMineInput(isNotEmpty)

  const {
    value: enteredEmail,
    isValid: enteredEmailIsValid,
    hasError: emailInputHaserror, 
    valueChangeHandler: emailInputChangeHandler, 
    valueBlurHandler: emailInputBlurHandler,
    reset: resetEmailInput 
  } = useMineInput(isEmail)

  let formIsValid = false

  if(enteredNameIsValid && enteredEmailIsValid && enteredLastNameIsValid) {
    formIsValid = true
  }

  const submitHandler = event => {
    event.preventDefault()
    if(!formIsValid) {
      return
    }

    console.log(enteredLastName)
    console.log(enteredName)
    console.log(enteredEmail)

    resetNameInput()
    resetEmailInput()
    resetLastNameInput()
  }

  const nameClasses = nameInputHaserror ? 'form-control invalid' : 'form-control'
  const lastNameClasses = lastNameInputHaserror ? 'form-control invalid' : 'form-control'
  const emailClasses = emailInputHaserror ? 'form-control invalid' : 'form-control'

  return (
    <form onSubmit={submitHandler}>
      <div className='control-group'>
        <div className={nameClasses}>
          <label htmlFor='name'>First Name</label>
          <input type='text' id='name' value={enteredName} onChange={nameInputChangeHandler} onBlur={nameInputBlurHandler} />
          {nameInputHaserror && <p className='error-text'>First name can't be empty.</p>}
        </div>
        <div className={lastNameClasses}>
          <label htmlFor='name'>Last Name</label>
          <input type='text' id='name' value={enteredLastName} onChange={lastNameInputChangeHandler} onBlur={lastNameInputBlurHandler}/>
          {lastNameInputHaserror && <p className='error-text'>Last name can't be empty.</p>}
        </div>
      </div>
      <div className={emailClasses}>
        <label htmlFor='name'>E-Mail Address</label>
        <input type='text' id='name' value={enteredEmail} onChange={emailInputChangeHandler} onBlur={emailInputBlurHandler}/>
        {emailInputHaserror && <p className='error-text'>Email is invalid</p>}
      </div>
      <div className='form-actions'>
        <button disabled={!formIsValid}>Submit</button>
      </div>
    </form>
  );
};

export default BasicForm;