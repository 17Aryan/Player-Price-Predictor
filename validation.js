function validation(values){
    let error={}
    const email_pattern= /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/
    const password_pattern=/^[a-zA-Z0-9!@#$%^&*]{8,}$/

    if(values.email===""){
        error.email="Email should not be empty"
    }
    else if(!email_pattern.test(values.email)){
        error.email="Email did't match"
    }
    else{
        error.email=""
    }
    if(values.password===""){
        error.password="Field should not be empty"
    }
    else if(!password_pattern.test(values.password)){
        error.password="Password didn't match"
    }
    else{
        error.password=""
    }
    return error

}
export default validation;