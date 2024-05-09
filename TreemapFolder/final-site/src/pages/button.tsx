import { useEffect, useState } from "react"
import React from 'react'
import './button.css'
import '../App.css'



const Button = () => {

   ['Consumer Defensive', 'Financial Services',
          'Healthcare', 'Industrials', 'Technology', 'Basic Materials',
           'Energy',  'Communication Services', 'Consumer Cyclical',
           'Utilities', 'Real Estate']
    


  const grab = (n) =>(
    fetch(`http://localhost:8080/api/${n}`),
    console.log('Fetching data')
  )
   

  

//chaneg buttons to navbar...
  return (
    <div className="div-style">
      <li>
        <button onClick={()=> grab('Technology')}>Technology</button>
        <button onClick={()=> grab('Energy')}>Energy</button>
        <button onClick={()=> grab('Real Estate')}>Real Estate</button>
        <button onClick={()=> grab('Consumer Defensive')}>Consumer Defensive</button>
        <button onClick={()=> grab('Financial Services')}>Financial Services</button>
        <button onClick={()=> grab('Healthcare')}>Healthcare</button>
        <button onClick={()=> grab('Industrials')}>Industrials</button>
        <button onClick={()=> grab('Basic Materials')}>Basic Materials</button>
        <button onClick={()=> grab('Communication Services')}>Communication Services</button>
        <button onClick={()=> grab('Consumer Cyclical')}>Consumer Cyclical</button>
        <button onClick={()=> grab('Utilities')}>Utilities</button>
      
      </li>

        
      
      
      
    
    
    </div>
    
      

    
  )
}

export default Button
