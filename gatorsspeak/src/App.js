import {Landing, NavBar, Dashboard} from './components';
import React from 'react';
import {Route, Routes} from "react-router-dom"
import "./App.css"
const App = () => (
  <div id='app-container'>
    <NavBar/>
    <Routes>
      <Route path='/' element = {<Landing/>} />
      <Route path='/dashboard' element = {<Dashboard/>} />
    </Routes>
  </div>
  )


export default App