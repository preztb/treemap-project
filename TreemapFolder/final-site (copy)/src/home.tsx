import React, {useState} from 'react'
import JsonDisplayData from './table'


import Button from './pages/button'




const Home = () => {

  const currDate = new Date().toLocaleDateString();
  const currTime = new Date().toLocaleTimeString();

  const [currentQuote, setCurrentQuote] = useState(currDate);

  const handleClick = () => {
    const randomIndex = Math.floor(Math.random() * currDate.length);
    setCurrentQuote(currDate);
  };
  

 
  return (
    <div>
      <h1>Market Capital as of {currDate} </h1>
      
      <div className='button-style'>
        <Button/>

      </div>
      
      <JsonDisplayData/>
      <button className='update-style' onClick={handleClick}>Update</button>
      <div id='generatedText'></div>
      
      
    </div>
  )
}

export default Home
