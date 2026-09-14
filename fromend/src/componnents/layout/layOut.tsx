import Header from "./Header"
import Footer from "./Footer"
import { Outlet } from "react-router"
import "./layOut.css"

export default function LayOut() {
  return (
    <div  className="layOutMain">
        <Header />
            <Outlet />
        <Footer />
    </div>
  )
}
