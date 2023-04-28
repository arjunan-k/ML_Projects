import classes from './Counter.module.css';
import { useDispatch, useSelector } from 'react-redux';
import { counterActions } from '../store';

const Counter = () => {
  const dispatch = useDispatch();
  const counter = useSelector(state => state.counter)
  const show = useSelector(state => state.showCounter)

  const incrementHandler = () => {
    // dispatch({type: 'increment'})
    dispatch(counterActions.increment())
  };

  const decrementHandler = () => {
    // dispatch({type: 'decrement'})
    dispatch(counterActions.decrement())
  };

  const increaseHandler = () => {
    // dispatch({type: 'increase', amount: 5 })
    // dispatch(counterActions.increase({amount: 5}))
    // { type: SOME_UNIQUE_IDENTIFIER, payload: 5 } 
    // dispatch(counterActions.increase(5))
    dispatch(counterActions.increase({amount: 5}))
  };

  const toggleCounterHandler = () => {
    // dispatch({type: "toggle"})
    dispatch(counterActions.toggleCounter())
  };

  return (
    <main className={classes.counter}>
      <h1>Redux Counter</h1>
      {show && <div className={classes.value}>{counter}</div>}
      <div>
        <button onClick={incrementHandler}>Increment</button>
        <button onClick={increaseHandler}>Increase by Five</button>
        <button onClick={decrementHandler}>Decrement</button>
      </div>
      <button onClick={toggleCounterHandler}>Toggle Counter</button>
    </main>
  );
};

export default Counter;