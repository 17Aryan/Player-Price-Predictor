import React, { useState } from 'react'
import { Link } from 'react-router-dom'
import Validation from './validation'

function Login() {
  const [values,setValues]=useState({
    email: '',
    password: ''
  })
  const [errors,setErrors]=useState({})
  const handleInput = (event)=>{
    setValues(prev =>({...prev,[event.target.name]:[event.target.value]}))
  }
  const handleSubmit=(event)=>{
    event.preventDefaault();
    setErrors(Validation(values))
  }
  return (
    <div className='d-flex justify-content-center align-items-center bg-primary vh-100'>
        <div className='bg-white p-3 rounded w-25'>
        <h2>Log-In</h2>
        <form action="" onSubmit={handleSubmit}>
            <div className='mb-3'>
                <label htmlFor="email">Email</label>
                <input type="email" placeholder='Email' name='email'
                onChange={handleInput} className='form-control rounded-0'/>
                {errors.email && <span className='text-danger'>{errors.email}</span>}
            </div>
            <div className='mb-3'>
                <label htmlFor="password">Password</label>
                <input type="password" placeholder='Password' name='password'
                onChange={handleInput} className='form-control rounded-0'/>
                {errors.password && <span className='text-danger'>{errors.password}</span>}
            </div>
            <button type='submit' className='btn btn-success w-100'>Log In</button>
            <p></p>
            <Link to="/signup" className='btn btn-default border w-100 bg-light text-decoration-none'>Create Account</Link>
        </form>
        </div>
    </div>
  )
}

export default Login
