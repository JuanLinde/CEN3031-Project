import React from 'react'
import {useState} from 'react'
import {logo} from '../assets'
import { flags } from '../constants'
import './Hero.css'
const Hero = () => {
  return (

    <div id='hero-container'>
      <div id='copy-and-gator'>
        <div id='hero-copy1'>
          <p id='learn'>
            Learn Language the Fun Way!
          </p>
          <p id='provides'>
            GatorsSpeak provides an engaging experience for kids seeking to learn new languages
          </p>
        </div>
        <img className='logo' src={logo} alt='gatorsspeak' width={593} height={461}/> 
      </div>
      <button id='get-started'> Get Started </button>
    </div>
  )
}

export default Hero