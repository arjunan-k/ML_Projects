import React from "react";
import { useContext, useEffect, useState } from "react";

const AuthContext = React.createContext({
    isLoggedIn: false,
    onLogout: () => {},
    onLogin: (email, password) => {}
})

export const AuthContextProvider = (props) => {
    const [isLoggedIn, setIsLoggedIn] = useState(false)

    useEffect(() => {
        const storedUserLoggedInInformation = localStorage.getItem('loggedIn')
    
        if(storedUserLoggedInInformation === '1') {
          setIsLoggedIn(true)
        }
      }, [])
    

    const logoutHandler = () => {
        localStorage.setItem('loggedIn', '0')
        setIsLoggedIn(false)
    }

    const loggedIn = () => {
        setIsLoggedIn(true)
    }

    const loginHandler = (email, password) => {
        localStorage.setItem('loggedIn', '1')
        setIsLoggedIn(true);
    };
    

    return (
        <AuthContext.Provider
            value={{isLoggedIn: isLoggedIn, onLogout: logoutHandler, onLogin: loginHandler}}>
            {props.children}
        </ AuthContext.Provider>
    )
}

export default AuthContext;