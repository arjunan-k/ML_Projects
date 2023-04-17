import { useState } from 'react';

const useMineInput = (validateValue) => {
    const[valueEntered, setValueEntered] = useState("")
    const [valueTouched, setValueTouched] = useState(false)

    const valueIsValid = validateValue(valueEntered)
    const hasError = !valueIsValid && valueTouched;

    const valueChangeHandler = (event) => {
        setValueEntered(event.target.value)
    }

    const valueBlurHandler = event => {
        setValueTouched(true)
    }

    const reset = () => {
        setValueTouched(false)
        setValueEntered("")
    }

    return {
        value: valueEntered,
        hasError,
        isValid: valueIsValid,
        reset,
        valueBlurHandler,
        valueChangeHandler   
    }
}

export default useMineInput;