import React from 'react'
import {useState} from 'react'
import {navLinks} from '../constants'
import {logo} from '../assets'
import './NavBar.css'
const NavBar = () => {
  return (
    <nav className='container'>
      <div className='logo-and-text'>
        <div className='logo-text'>
          <span id='gators'>Gators</span><span id='speak'>Speak</span>
        </div>
        <img className='logo' src={logo} alt='gatorsspeak' width={80} height={62}/> 
      </div>
      {navLinks.map((nav, index) => (
          <a key={nav.id} href={`#${nav.id}`}>
            {nav.title}
          </a>
      ))}
    </nav>
  )
}

export default NavBar