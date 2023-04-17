// import useInput from "../hooks/user-input";
import useInput from "../hooks/user-input-reducer";

const SimpleInput = (props) => {
  const {
    value: enteredName, 
    isValid: enteredNameIsValid,
    hasError: nameInputHaserror, 
    valueChangeHandler: nameInputChangeHandler, 
    inputBlurHandler: nameInputBlurHandler,
    reset: resetNameInput 
  } = useInput(value => value.trim() !== "")

  const {
    value: enteredEmail, 
    isValid: enteredEmailIsValid,
    hasError: emailInputHaserror, 
    valueChangeHandler: emailInputChangeHandler, 
    inputBlurHandler: emailInputBlurHandler,
    reset: resetEmailInput 
  } = useInput(value => value.trim().length > 0 && value.trim().includes('@'))

  let formIsValid = false;

  if (enteredNameIsValid && enteredEmailIsValid) {
    formIsValid = true;
  }

  const formSubmissionHandler = (event) => {
    event.preventDefault();

    if (!enteredNameIsValid || !enteredEmailIsValid) {
      return;
    }
    console.log(enteredName);
    console.log(enteredEmail)
    resetNameInput()
    resetEmailInput()
  };

  const nameInputClasses = nameInputHaserror ? 'form-control invalid' : 'form-control'
  const emailInputClasses = emailInputHaserror ? 'form-control invalid' : 'form-control'

  return (
    <form onSubmit={formSubmissionHandler}>
      <div className={nameInputClasses}>
        <label htmlFor='name'>Your Name</label>
        <input
          type='text'
          id='name'
          onChange={nameInputChangeHandler}
          onBlur={nameInputBlurHandler}
          value={enteredName}/>
        {nameInputHaserror && (<p className='error-text'>Name must not be empty.</p>)}
      </div>

      <div className={emailInputClasses}>
        <label htmlFor='email'>Your Email</label>
        <input
          type='text'
          id='email'
          onChange={emailInputChangeHandler}
          onBlur={emailInputBlurHandler}
          value={enteredEmail}/>
        {emailInputHaserror && (<p className='error-text'>Please enter a valid email.</p>)}
      </div>
      <div className='form-actions'>
        <button disabled={!formIsValid}>Submit</button>
      </div>
    </form>
  );
};

export default SimpleInput;