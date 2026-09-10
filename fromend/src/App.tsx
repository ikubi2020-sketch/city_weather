import './App.css'
import {Routes ,Route} from "react-router" 
import { ProtectedRoute } from './componnents/protectedRoute/protectedRoute'
import Enter from './componnents/enter/Enter'

function App() {

  return (
    <>
      <Routes>

        <Route path="/enter" />
        <Route />
        <Route />

        <Route path='*'>400, something went wrong</Route>
      </Routes>
    </>
  )
}

export default App
