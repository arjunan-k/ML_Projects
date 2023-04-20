import React from 'react';
import Login from './components/Login/Login';
import Home from './components/Home/Home';
import MainHeader from './components/MainHeader/MainHeader';
import AuthContext from './store/auth-context';
import { useState } from 'react';
import { useContext } from 'react';

function App() {

  // const [isLoggedIn, setIsLoggedIn] = useState(false);

  // useEffect(() => {
  //   const storedUserLoggedInInformation = localStorage.getItem('loggedIn')

  //   if(storedUserLoggedInInformation === '1') {
  //     setIsLoggedIn(true)
  //   }
  // }, [])

  // const loginHandler = (email, password) => {
  //   localStorage.setItem('loggedIn', '1')
  //   setIsLoggedIn(true);
  // };

  // const logoutHandler = () => {
  //   localStorage.setItem('loggedIn', '0')
  //   setIsLoggedIn(false);
  // };

  const ctx = useContext(AuthContext)

  return (
  <React.Fragment>
    <MainHeader/>
      <main>
        {!ctx.isLoggedIn && <Login />}
        {ctx.isLoggedIn && <Home />}
      </main>
  </React.Fragment>
  );
}

export default App;