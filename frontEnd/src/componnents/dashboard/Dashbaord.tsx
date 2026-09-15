
export default function DashBoard() {
    const userName =  localStorage.getItem("userName")
  return (
    <div>
        <h1>hello {userName}</h1>
        
    </div>
  )
}
