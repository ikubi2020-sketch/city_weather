import './App.css'
import {Routes ,Route} from "react-router" 


function App() {

  return (
    <>
      <Routes>
        
        <Route />
        <Route />
        <Route />

        <Route path='*'>400, something went wrong</Route>
      </Routes>
    </>
  )
}

export default App
