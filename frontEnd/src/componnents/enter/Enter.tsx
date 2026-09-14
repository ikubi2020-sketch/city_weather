import  { useState, type SubmitEvent } from 'react';
import { useNavigate } from 'react-router';

export default function Enter() {
    const [userName, setUserName] = useState("")
    const navigate = useNavigate()
   const handelSubmit = (e : SubmitEvent<HTMLFormElement>) => {
      e.preventDefault()
      if(userName.trim()!==  ""){
        localStorage.setItem("userName", userName)
        navigate("/dashboard")
      }
    }

  return (
    <div>
        <h1>welcome to weather website</h1>
        <h2>to access please enter user name</h2>
        <form onSubmit={handelSubmit}>
          <input type="text" placeholder="your name" 
          value={userName}
          onChange={e => setUserName(e.target.value)}/>
          <button type='submit'>ENTER</button>
        </form>
    </div>
  )
}
