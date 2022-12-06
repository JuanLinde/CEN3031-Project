import React from 'react'
import {NavBar, Hero, Features} from './'
import {Link} from 'react-router-dom'
import './Landing.css'
const Landing = () => {
  return (
    <div className='landing'>
        <Hero/>
        <Features/>
    </div>
  )
}

export default Landing