import { useEffect, useState } from 'react'

// import reactLogo from './assets/react.svg'
// import viteLogo from './assets/vite.svg'
// import heroImg from './assets/hero.png'
// import './App.css'

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then(response => response.json())
      .then(data => setData(data))
      .catch(error => console.log("ERROR FETCHING DATA : ", error))
  }, [])

  return (
    <>
      <div> <h1>CORS Handling Demo</h1> This is a simple React app that demonstrates CORS handling with a FastAPI backend. </div>
      <hr />
      <div>
        {
          data ? (
            <p>MESSAGE : {data.message}</p>
          ) : (
            <p>LOADING.....</p>)
        }
      </div>
    </>
  )
}

export default App
