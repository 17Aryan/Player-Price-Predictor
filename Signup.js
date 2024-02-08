import React,{useState} from 'react'
import { Link, useNavigate } from 'react-router-dom'
import Validation from './validation'
import axios from 'axios'
function Signup() {
    const [values,setValues]=useState({
        name:'',
        email: '',
        password: ''
      })
      const navigate=useNavigate();
      const [errors,setErrors]=useState({})
      const handleInput = (event)=>{
        setValues(prev =>({...prev,[event.target.name]:[event.target.value]}))
      }
      const handleSubmit=(event)=>{
        event.preventDefaault();
        setErrors(Validation(values));
        if(errors.name==="" && errors.email==="" && errors.password===""){
            axios.post('http://http://localhost:8081/signup',values)
            .then(res=>{
                navigate('/');
            })
            .catch(err=>console.log(err));
        }
      }
  return (
    <div className='d-flex justify-content-center align-items-center bg-primary vh-100'>
        <div className='bg-white p-3 rounded w-25'>
        <h2>Registration</h2>
        <form action="" onSubmit={handleSubmit}>
            <div className='mb-3'>
                <label htmlFor="name">Name</label>
                <input type="text" placeholder='Name' name='name' 
                onChange={handleInput} className='form-control rounded-0'/>
                {errors.name && <span className='text-danger'>{errors.name}</span>}
            </div>
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
            <button className='btn btn-success w-100'>Sign Up</button>
            <p></p>
            <Link to="/" className='btn btn-default border w-100 bg-light text-decoration-none'>Login</Link>
        </form>
        </div>
    </div>
  )
}

export default Signup