import React from 'react'
import Login from './login'
import {
  Router,Routes, Route
} from 'react-router-dom'
import Signup from './Signup'

function app() {
  return (
    <Router>
      <Routes>
        <Route path='/' element={ <Login />}></Route>
        <Route path='/signup' element={ <Signup />}></Route>
      </Routes>
    </Router>
  )
}
export default app
