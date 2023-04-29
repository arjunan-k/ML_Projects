// import { createStore } from 'redux';

// const counterReducer = (state = initialState, action) => {

//     if(action.type === "increment") {
//         return {
//             counter: state.counter + 1,
//             showCounter: state.showCounter,
//         }
//     }

//     if(action.type === "decrement") {
//         return {
//             counter: state.counter - 1,
//             showCounter: state.showCounter,
//         }
//     }

//     if(action.type === "increase") {
//         return {
//             counter: state.counter + action.amount,
//             showCounter: state.showCounter,
//         }
//     }

//     if(action.type === "toggle") {
//         return {
//             counter: state.counter,
//             showCounter: !state.showCounter,
//         }
//     }

//     return state
// } 

// const store = createStore(counterReducer);

import { configureStore } from '@reduxjs/toolkit'
import counterReducer from './counter'
import authSlice from './auth';

const store = configureStore({
    reducer: { 'counter': counterReducer, 'auth': authSlice.reducer }
})

export default store;