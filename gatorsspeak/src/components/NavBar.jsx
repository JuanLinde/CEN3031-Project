import React from 'react'
import {useState} from 'react'
import {navLinks} from '../constants'
import {logo} from '../assets'
import '../NavBar.css'
const NavBar = () => {
  return (
    <nav className='container'>
      <p className='logo-text'>
        GatorsSpeak
      </p>
      <img src={logo} alt='gatorsspeak' width={80} height={62}> 
      </img>
      <p className='nav-p'>
        Dashboard
      </p>
      <p className='nav-p'>
        Login
      </p>
      <p className='nav-p'>
        SignUp
      </p>
    </nav>
  )
}

export default NavBar