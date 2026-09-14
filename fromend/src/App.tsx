import './App.css'
import {Routes ,Route} from "react-router" 
// import { ProtectedRoute } from './componnents/protectedRoute/protectedRoute'
// import Enter from './componnents/enter/Enter'
import LayOut from './componnents/layout/layOut'


function App() {

  return (
    <>
      <Routes>
        <Route element={<LayOut/>}>
          <Route path="/enter"/>
          
            <Route path="/" />
            <Route />
            <Route path='*'>400, something went wrong</Route>

        </Route>
      </Routes>
    </>
  )
}

export default App
