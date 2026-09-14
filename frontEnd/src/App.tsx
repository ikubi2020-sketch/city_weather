import './App.css'
import {Routes ,Route} from "react-router" 
import { ProtectedRoute } from './componnents/protectedRoute/protectedRoute'
import Enter from './componnents/enter/Enter'
import DashBoard from './componnents/dashboard/Dashbaord'
import Favorites from './componnents/favorites/Favorites'
import Compare from './componnents/compare/compare'
import LayOut from './componnents/layout/layOut'
import Search from './componnents/search/Search'


function App() {

  return (
    <>
      <Routes>
        
          <Route path="/enter" element={<Enter/>}/>

          <Route element={<LayOut/>}>
          
              <Route path="/dashboard" element={
                <ProtectedRoute>
                  <DashBoard/>                                    
                </ProtectedRoute>
              }/>
            
              <Route path="/search" element={
                <ProtectedRoute>
                  <Search/>
                </ProtectedRoute>
              }/>
              
              <Route path="/favorite" element={
                <ProtectedRoute>
                  <Favorites/>
                </ProtectedRoute>
              }/>
              
              <Route path="/compare" element={
                <ProtectedRoute>
                  <Compare/>
                </ProtectedRoute>
              }/>

          <Route path='*'>400, something went wrong</Route>

        </Route>
      </Routes>
    </>
  )
}

export default App
