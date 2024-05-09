import "./App.css";
import React from "react";
import { Routes, Link, useLocation} from "react-router-dom";
import { Route } from "react-router-dom";
import Home from "./home";
import Page2 from "./page2";










const App = () => {


  return (
    <>
    
      <Routes>
        <Route path='/' element={<Home/>}/>
      </Routes>
    </>
    
      
            
            

            
            
            
    
  );
}

export default App
